# A3-Server-Modlist-Tools
A set of methods that you could find useful if you're manually setting up a modded Arma 3 server on Linux. 

It *should* work on Windows but I've only tested it on Ubuntu and the one piece of code that is be Linux specific will not be executed on Windows anyways.

A simple menu is included if you'd like to pick which method you'd like to run. 

The script can:
- Read and export the mod IDs from a standard Arma 3 modlist .html file.
- Setup a download script for steamcmd.
- Run the generated script with an existing steamcmd installation.
- Go through all the mod files in your Arma steam workshop directory and make them lowercase (Linux only)
- Symlink all the mods from the workshop directory to the server directory.
- Generate a mod string which would be passed in the form of the mod= parameter to the Arma 3 server executable (or client executable)
All of the above can be ran by just selecting option 1 and waiting for the operations to complete (the download and renaming of files can take a while).

The script can also delete mods and symlinks that are not in the currently selected modlist if you'd like to save space on your server.

## Requirements
Python 3.12 was used for this project and all the libraries should be a part of a standard Python installation.

To use all the scripts, you'd want a Windows/Linux server setup with steamcmd already setup.

You need to login into the Steam account you want to use for steamcmd at least once before using any scripts, that account must own Arma 3 in order to download workshop mods.

## Usage
Set the variables at the top of the Python script.
Run the Python script through a terminal of your choosing with `python core.py` or `python3 core.py` and use the menu options.

