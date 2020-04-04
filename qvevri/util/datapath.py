"""Utility to get the path of Qvevri assets"""
import os
import sys
from qvevri.util import system


def get():
    """Return the path for the resources."""
    launch_path = os.path.realpath(sys.path[0])
    if launch_path.startswith("/usr/local"):
        data_path = "/usr/local/share/qvevri"
    elif launch_path.startswith("/usr"):
        data_path = "/usr/share/qvevri"
    elif system.path_exists(os.path.normpath(os.path.join(sys.path[0], "share"))):
        data_path = os.path.normpath(os.path.join(sys.path[0], "share/qvevri"))
    elif system.path_exists(os.path.normpath(os.path.join(launch_path, "../../share/qvevri"))):
        data_path = os.path.normpath(os.path.join(launch_path, "../../share/qvevri"))
    else:
        import qvevri

        qvevri_module = qvevri.__file__
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(qvevri_module)), "share/qvevri"
        )
    if not system.path_exists(data_path):
        raise IOError("data_path can't be found at : %s" % data_path)
    return data_path
