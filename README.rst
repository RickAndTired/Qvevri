******
Qvevri
******
.. image:: https://i.imgur.com/DMI4nXC.png

Qvevri is a basic Wine Manager forked from Lutris

**Dependencies:**

Wine

Python 3 (PyGObject3 and PyYAML)

**Download and extract Qvevri**

Run **Qvevri-Launcher** or **bin/qvevri**

**Locations**

~/.local/share/qvevri/

~/.local/share/qvevri/runners/wine/

~/.config/qvevri/

**Screenshot**

.. image:: https://i.imgur.com/aoUV3nW.png

******
ToDo
******
/share/qvevri/ui/qvevri-window.ui

- [x] hide account button
- [x] hide website search 
- [x] hide view sorting options
- [x] hide options "Installed Games Only" through "Show Tray Icon" other than Dark Theme, Manager Runners, and About
- [x] rename "About Qvevri"
- [x] rename "Add Game"
- [x] hide "Import Games"
- [x] rename "Search Games"

/qvevri/gui/qvevriwindow.py

- [x] hide left side panel by default
- [x] hide right side panel by default
- [x] set default runner to wine

/qvevri/startup.py

- [x] hide pop ups
- [x] remove vulkan pop up
- [x] change driver message
- [x] create defaultbottle directory
- [x] create default installation directory

/qvevri/gui/config/common.py

- [x] remove confirm runner change
- [x] rename "Game options"
- [x] rename "Game info"
- [] hide release year (causes error)

/qvevri/runners/__init__.py

- [x] hide all runners except wine and linux

/qvevri/runners/wine.py

- [x] set default wine prefix/bottle
- [x] rename wine prefix to wine bottle
- [x] move arguments to below Wine Version in Options tab
- [x] hide various options
- [x] hide various options to "advanced"
- [x] reorganize options
- [x] reword to "Wine (Runs Windows Programs)"

/qvevri/runners/linux.py
- [x] reword to "Linux (Runs Native Programs)"

/qvevri/game_actions.py

- [x] rename Play to "Start Program"
- [x] hide show logs
- [x] hide install another version
- [x] hide view on qvevri
- [x] hide "hide game"

/qvevri/gui/views/list.py

- [x] hide all columns other than Name

/qvevri/gui/config/add_game.py

- [x] rename "Add a new game"

/qvevri/sysoptions.py

- [x] change defualt installation directory
- [x] hide everything other than Gamemode, ACO, and Environment variables to "advanced"
- [x] remove "condition" line from gamemode


Other

- [x] rename
- [x] about page
- [x] create default wine bottle
- [x] change config directory
- [x] replace icons/artwork
- [x] add launcher to root dir
- [x] move files to docs directory
- [] Wine "Manage Versions" change server
- [] snapcraft
- [] remove unused code
- [] remove unused files
- [] text clean up
- [] name clean up
- [] add toggle for DXVK_HUD
- [] change remove button


Long-term ToDo / unlikly wish list

- [] Simplify - create Wine Bottle - Run installer - Create program listing
- [] Left side panel - Wine Bottle selection
- [] Winetricks checkbox UI to see what is already installed
- [] Winetricks bundles
- [] Wine downloader

