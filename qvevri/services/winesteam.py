"""Steam for Windows service"""
from qvevri.services.steam import SteamSyncer

NAME = "Steam for Windows"
ICON = "winesteam"
ONLINE = False


class WineSteamSyncer(SteamSyncer):
    """Sync games with Steam for Windows"""
    platform = "windows"


SYNCER = WineSteamSyncer
