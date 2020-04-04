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

- [] rename
- [] about page
- [] create default wine bottle
- [] change config directory
- [] replace icons/artwork
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


******
Qvevri
******

|LiberaPayBadge|_



Qvevri is an open source gaming platform that makes gaming on Linux easier by
managing, installing and providing optimal settings for games.

Qvevri does not sell games. For commercial games, you must own a copy to install
the game on Qvevri.
The platform uses programs referred to as 'runners' to launch games,
Those runners (with the exception of Steam and web browsers) are provided and
managed by Qvevri, so you don't need to install them with your package manager.

Scripts written by the community allow access to a library of games.
Using scripts, games can be played without manual setup.

Installer scripts
=================

Qvevri installations are fully automated through scripts, which can be written
in either JSON or YAML.
The scripting syntax is described in ``docs/installers.rst``, and is also
available online at `qvevri.net <https://qvevri.net>`_.

Game library
============

Optional accounts can be created at `qvevri.net
<https://qvevri.net>`_ and linked with Qvevri clients.
This enables your client to automatically sync fetch library from the website.
**It is currently not possible to sync from the client to the cloud.**
Via the website, it is also possible to sync your Steam library to your Qvevri
library.

The Qvevri client only stores a token when connected with the website, and your
login credentials are never saved.
This token is stored in ``~/.cache/qvevri/auth-token``.

Configuration files
===================

* ``~/.config/qvevri``: The client, runners, and game configuration files

   There is be no need to manually edit these files as everything should be done from the client.

* ``qvevri.conf``: Preferences for the client's UI

* ``system.yml``: Default game configuration, which applies to every game

* ``runners/*.yml``: Runner-specific configurations

* ``games/*.yml``: Game-specific configurations

Game-specific configurations overwrite runner-specific configurations, which in
turn overwrite the system configuration.

Runners and the game database
=============================

``~/.local/share/qvevri``: All data necessary to manage Qvevri' library and games, including:

* ``pga.db``: An SQLite database tracking the game library, game installation status, various file locations, and some additional metadata

* ``runners/*``: Runners downloaded from `qvevri.net <https://qvevri.net>`

* ``banners/*.jpg``: Game banners

``~/.local/share/icons/hicolor/128x128/apps/qvevri_*.png``: Game icons

Command line options
====================

The following command line arguments are available::

-v, --version              Print the version of Qvevri and exit
-d, --debug                Show debug messages
-i, --install              Install a game from a yml file
-e, --exec                 Execute a program with the qvevri runtime
-l, --list-games           List all games in database
-o, --installed            Only list installed games
-s, --list-steam-games     List available Steam games
--list-steam-folders       List all known Steam library folders
-j, --json                 Display the list of games in JSON format
--reinstall                Reinstall game
--display=DISPLAY          X display to use

Additionally, you can pass a ``qvevri:`` protocol link followed by a game
identifier on the command line such as::

    qvevri qvevri:quake

This will install the game if it is not already installed, otherwise it will
launch the game. The game will always be installed if the ``--reinstall`` flag is passed.

Planned features
================

Qvevri is far from complete, and some features have yet
to be implemented.

Here's what to expect from future versions of Qvevri:

* TOSEC database integration
* Management of personal game data (i.e. syncing games across devices using private cloud storage)
* Community features (friends list, chat, multiplayer game scheduling, etc.)

Support the project
===================

Qvevri is 100% community supported, to ensure a continuous development on the
project, please consider donating to the project.
Our main platform for supporting Qvevri is Patreon: https://www.patreon.com/qvevri
but there are also other options available at https://qvevri.net/donate

Come with us!
=============

Want to make Qvevri better? Help implement features, fix bugs, test
pre-releases, or simply chat with the developers?

You can always reach us on:

* Discord: https://discordapp.com/invite/Pnt5CuY
* IRC: #qvevri on the Freenode servers
* Github: https://github.com/qvevri
* Twitter: https://twitter.com/QvevriGaming


.. |LiberaPayBadge| image:: http://img.shields.io/liberapay/receives/Qvevri.svg?logo=liberapay
.. _LiberaPayBadge: https://liberapay.com/Qvevri/
