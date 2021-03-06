"""Check to run at program start"""
# pylint: disable=no-member
import os
from qvevri.util.log import logger
from qvevri import pga
from qvevri.game import Game
from qvevri import settings
from qvevri.util.system import create_folder
from qvevri.util.graphics import drivers
from qvevri.util.graphics import vkquery
from qvevri.util.linux import LINUX_SYSTEM
from qvevri.gui.dialogs import DontShowAgainDialog


def init_dirs():
    """Creates Qvevri directories"""
    directories = [
        settings.CONFIG_DIR,
        os.path.join(settings.CONFIG_DIR, "runners"),
        os.path.join(settings.CONFIG_DIR, "games"),
        settings.DATA_DIR,
        os.path.join(settings.DATA_DIR, "covers"),
        settings.ICON_PATH,
        os.path.join(settings.DATA_DIR, "banners"),
        os.path.join(settings.DATA_DIR, "coverart"),
        os.path.join(settings.DATA_DIR, "runners"),
        os.path.join(settings.DATA_DIR, "defaultbottle"),
        os.path.join(settings.DATA_DIR, "programs"),
        os.path.join(settings.DATA_DIR, "lib"),
        settings.RUNTIME_DIR,
        settings.CACHE_DIR,
        os.path.join(settings.CACHE_DIR, "installer"),
        os.path.join(settings.CACHE_DIR, "tmp"),
    ]
    for directory in directories:
        create_folder(directory)


def init_db():
    """Initialize the SQLite DB"""
    pga.syncdb()


def init_qvevri():
    """Run full initialization of Qvevri"""
    init_dirs()
    init_db()


def check_driver():
    """Report on the currently running driver"""
    driver_info = {}
    if drivers.is_nvidia():
        driver_info = drivers.get_nvidia_driver_info()
        # pylint: disable=logging-format-interpolation
        logger.info(
            "Using {vendor} drivers {version} for {arch}".format(**driver_info["nvrm"])
        )
        gpus = drivers.get_nvidia_gpu_ids()
        for gpu_id in gpus:
            gpu_info = drivers.get_nvidia_gpu_info(gpu_id)
            logger.info("GPU: %s", gpu_info.get("Model"))
    elif LINUX_SYSTEM.glxinfo:
        logger.info("Using %s", LINUX_SYSTEM.glxinfo.opengl_vendor)
        if hasattr(LINUX_SYSTEM.glxinfo, "GLX_MESA_query_renderer"):
            logger.info(
                "Running Mesa driver %s on %s",
                LINUX_SYSTEM.glxinfo.GLX_MESA_query_renderer.version,
                LINUX_SYSTEM.glxinfo.GLX_MESA_query_renderer.device,
            )
    else:
        logger.warning(
            "glxinfo is not available on your system, unable to detect driver version"
        )

    for card in drivers.get_gpus():
        # pylint: disable=logging-format-interpolation
        try:
            logger.info(
                "GPU: {PCI_ID} {PCI_SUBSYS_ID} using {DRIVER} drivers".format(
                    **drivers.get_gpu_info(card)
                )
            )
        except KeyError:
            logger.error("Unable to get GPU information from '%s'", card)

    if drivers.is_outdated():
        setting = "hide-outdated-nvidia-driver-warning"
        if settings.read_setting(setting) != "True":
            DontShowAgainDialog(
                setting,
                "Your Nvidia driver is outdated.",
                secondary_message="You are currently running driver %s which does not "
                "fully support all features for Vulkan and DXVK games.\n"
                "Please upgrade your driver",
            )


def check_libs(all_components=False):
    """Checks that required libraries are installed on the system"""
    missing_libs = LINUX_SYSTEM.get_missing_libs()
    if all_components:
        components = LINUX_SYSTEM.requirements
    else:
        components = LINUX_SYSTEM.critical_requirements
    missing_vulkan_libs = []
    for req in components:
        for index, arch in enumerate(LINUX_SYSTEM.runtime_architectures):
            for lib in missing_libs[req][index]:
                if req == "VULKAN":
                    missing_vulkan_libs.append(arch)
                logger.error("%s %s missing (needed by %s)", arch, lib, req.lower())

#    if missing_vulkan_libs:
#        setting = "dismiss-missing-vulkan-library-warning"
#        if settings.read_setting(setting) != "True":
#            DontShowAgainDialog(
#                setting,
#                "Missing vulkan libraries",
#                secondary_message="Qvevri was unable to detect Vulkan support for "
#                "the %s architecture.\n"
#                "This will prevent many games and some programs from working.",
#            )


def check_vulkan():
    """Reports if Vulkan is enabled on the system"""
    if vkquery.is_vulkan_supported():
        logger.info("Vulkan is supported")
    else:
        logger.info("Vulkan is not available or your system isn't Vulkan capable")


def check_donate():
    setting = "dont-support-qvevri"
    if settings.read_setting(setting) != "True":
        DontShowAgainDialog(
            setting,
            "Please support Qvevri!",
            secondary_message="Qvevri is entirely funded by its community and will "
            "remain an independent gaming platform.\n"
            "For Qvevri to survive and grow, the project needs your help.\n"
            "Please consider making a donation if you can. This will greatly help "
            "cover the costs of hosting the project and fund new features "
            "like cloud saves or a full-screen interface for the TV!\n"
            "<a href='https://qvevri.net/donate'>SUPPORT US! https://qvevri.net/donate</a>",
        )


def fill_missing_platforms():
    """Sets the platform on games where it's missing.
    This should never happen.
    """
    pga_games = pga.get_games(filter_installed=True)
    for pga_game in pga_games:
        if pga_game.get("platform") or not pga_game["runner"]:
            continue
        game = Game(game_id=pga_game["id"])
        logger.error("Providing missing platform for game %s", game.slug)
        game.set_platform_from_runner()
        if game.platform:
            game.save(metadata_only=True)


def run_all_checks():
    """Run all startup checks"""
    check_driver()
    check_libs()
    check_vulkan()
#    check_donate()
    fill_missing_platforms()
