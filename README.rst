******
Qvevri
******
Qvevri is a basic Wine Manager forked from Qvevri

ToDo

/share/qvevri/ui/qvevri-window.ui

- [x] hide account button
- [x] hide website search 
- [x] hide view sorting options
- [x] hide options "Installed Games Only" through "Show Tray Icon" other than Dark Theme and About
- [x] rename "About Qvevri"
- [x] rename "Add Game"
- [x] hide "Import Games"

/qvevri/gui/qvevriwindow.py

- [x] hide left side panel by default
- [x] hide right side panel by default

/qvevri/startup.py

- [x] hide donate pop up

/qvevri/gui/config/common.py

- [x] hide install runner
- [] hide release year (causes error)

/qvevri/runners/__init__.py

- [x] hide all runners except wine

/qvevri/runners/wine.py

- [] set default wine prefix/bottle
- [x] rename wine prefix to wine bottle
- [x] move arguments to below Wine Version in Options tab
- [x] hide various options
- [x] hide various options to "advanced"
- [x] reorganize options

/qvevri/game_actions.py

- [x] rename Play to "Start Program"
- [x] hide show logs
- [x] hide install another version
- [x] hide view on qvevri
- [x] hide "hide game"

/qvevri/gui/views/list.py

- [x] hide all columns other than Name

/qvevri/sysoptions.py

- [] change defualt installation folder
- [x] hide everything other than Gamemode, ACO, and Environment variables to "advanced"
- [x] remove "condition" line from gamemode

Other

- [x] rename
- [x] about page
- [x] create default wine bottle
- [x] change config directory
- [x] replace icons/artwork
- [] snapcraft
- [] remove unused code
- [] remove unused files
- [] text clean up
- [] name clean up
- [] set default runner to wine / hide runner selection



Long-term ToDo / unlikly wish list

- [] Simplify - create Wine Bottle - Run installer - Create program listing
- [] Winetricks checkbox UI to see what is already installed
- [] Winetricks bundles
- [] Wine downloader
