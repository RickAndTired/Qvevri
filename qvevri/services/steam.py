"""Steam service"""
import os
import re

from qvevri import pga
from qvevri.config import make_game_config_id, QvevriConfig
from qvevri.util.steam.appmanifest import AppManifest, get_appmanifests
from qvevri.util.steam.config import get_steamapps_paths
from qvevri.services.service_game import ServiceGame

NAME = "Steam"
ICON = "steam"
ONLINE = False


class SteamGame(ServiceGame):
    """ServiceGame for Steam games"""

    store = "steam"
    installer_slug = "steam"
    excluded_appids = [
        "228980",  # Steamworks Common Redistributables
        "1070560",  # Steam Linux Runtime
    ]

    @classmethod
    def new_from_steam_game(cls, appmanifest, game_id=None):
        """Return a Steam game instance from an AppManifest"""
        steam_game = SteamGame()
        steam_game.appid = str(appmanifest.steamid)
        steam_game.game_id = game_id
        steam_game.name = appmanifest.name
        steam_game.slug = appmanifest.slug
        steam_game.runner = appmanifest.get_runner_name()
        return steam_game

    @classmethod
    def new_from_qvevri_id(cls, game_id):
        steam_game = SteamGame()
        steam_game.game_id = game_id
        return steam_game

    @property
    def config_id(self):
        return make_game_config_id(self.slug)

    @classmethod
    def is_importable(cls, appmanifest):
        """Return whether a Steam game should be imported"""
        if not appmanifest.is_installed():
            return False
        if appmanifest.steamid in cls.excluded_appids:
            return False
        if re.match(r"^Proton \d*", appmanifest.name):
            return False
        return True

    def create_config(self):
        """Create the game configuration for a Steam game"""
        game_config = QvevriConfig(
            runner_slug=self.runner, game_config_id=self.config_id
        )
        game_config.raw_game_config.update({"appid": self.appid})
        game_config.save()


class SteamSyncer:
    """Sync Steam games to the local library"""
    platform = "linux"

    def __init__(self):
        self._qvevri_games = None
        self._qvevri_steamids = None

    @property
    def runner(self):
        """Return the appropriate runner for the platform"""
        return "steam" if self.platform == "linux" else "winesteam"

    @property
    def qvevri_games(self):
        """Return all Steam games present in the Qvevri library"""
        if not self._qvevri_games:
            self._qvevri_games = pga.get_games_where(
                steamid__isnull=False, steamid__not=""
            )
        return self._qvevri_games

    @property
    def qvevri_steamids(self):
        """Return the Steam IDs of the games installed in Qvevri"""
        if not self._qvevri_steamids:
            self._qvevri_steamids = {str(game["steamid"]) for game in self.qvevri_games}
        return self._qvevri_steamids

    def load(self):
        """Return importable Steam games"""
        games = []
        steamapps_paths = get_steamapps_paths()
        for steamapps_path in steamapps_paths[self.platform]:
            for appmanifest_file in get_appmanifests(steamapps_path):
                app_manifest = AppManifest(
                    os.path.join(steamapps_path, appmanifest_file)
                )
                if SteamGame.is_importable(app_manifest):
                    games.append(SteamGame.new_from_steam_game(app_manifest))
        return games

    def get_pga_game(self, game):
        """Return a PGA game if one is found"""
        for pga_game in self.qvevri_games:
            if (
                    str(pga_game["steamid"]) == game.appid
                    and (pga_game["runner"] == self.runner or not pga_game["runner"])
                    and not pga_game["installed"]
            ):
                return pga_game

    def sync(self, games, full=False):
        """Syncs Steam games to Qvevri"""
        available_ids = set()  # Set of Steam appids seen while browsing AppManifests
        added_games = []
        for game in games:
            steamid = game.appid
            available_ids.add(steamid)
            pga_game = self.get_pga_game(game)

            if pga_game:
                if (
                        steamid in self.qvevri_steamids
                        and pga_game["installed"] != 1
                        and pga_game["installed"]
                ):
                    added_games.append(game.install())

            if steamid not in self.qvevri_steamids:
                added_games.append(game.install())
            else:
                if pga_game:
                    added_games.append(game.install(pga_game))

        if not full:
            return added_games, games

        removed_games = []
        unavailable_ids = self.qvevri_steamids.difference(available_ids)
        for steamid in unavailable_ids:
            for pga_game in self.qvevri_games:
                if (
                        str(pga_game["steamid"]) == steamid
                        and pga_game["installed"]
                        and pga_game["runner"] == self.runner
                ):
                    game = SteamGame.new_from_qvevri_id(pga_game["id"])
                    game.uninstall()
                    removed_games.append(pga_game["id"])
        return (added_games, removed_games)


SYNCER = SteamSyncer
