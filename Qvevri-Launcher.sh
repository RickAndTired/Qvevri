#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Main entry point for Qvevri"""
import sys
import locale
import os
from os.path import realpath, dirname, normpath

LAUNCH_PATH = dirname(realpath(__file__))

if os.path.isdir(os.path.join(LAUNCH_PATH, "../qvevri")):
    sys.dont_write_bytecode = True
    SOURCE_PATH = normpath(os.path.join(LAUNCH_PATH, '..'))
    sys.path.insert(0, SOURCE_PATH)
else:
    sys.path.insert(0, os.path.normpath(os.path.join(LAUNCH_PATH, "../lib/qvevri")))

try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    sys.stderr.write("Unsupported locale setting. Fix your locales\n")

from qvevri.gui.application import Application

app = Application()  # pylint: disable=invalid-name
sys.exit(app.run(sys.argv))
