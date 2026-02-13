# Lego Games save file checksum update
This project is a fork of LSWSCU by Polly May, originally available at:
https://github.com/pollyevamay/LSWSCU.

This program extends the original tool by adding support for additional LEGO games (PC/Mac only) and includes minor improvements, such as displaying both hexadecimal and decimal values for the old and new checksum values.

## Supported Save Files
This program can be used on all platforms for the following games:
- Lego Star Wars: The Video Game
- Lego Star Wars II: The Original Trilogy
- Lego Star Wars: The Complete Saga

For PC/Mac only, this program also supports:
- Lego Indiana Jones: The Original Adventures
- Lego Batman: The Video Game
- Lego Indiana Jones 2: The Adventure Continues

## What this tool does
- Recalculates and updates save file checksums
- Ensures modified save files remain valid and load correctly in-game
- Displays checksum values in both hexadecimal and decimal formats

## How to use?
Simply drag your save onto the "Drag save file onto me!" python script (python required) or .exe file. This will generate a new checksum for the save file, which will pass the checksum check that the game will perform when loading a save file, allowing you to use it.

ALWAYS MAKE BACKUPS OF YOUR SAVE FILES. YOU TAKE RESPONSIBILITY FOR WHAT HAPPENS TO THEM.

## Finding your save files? (PC/Mac)
- Lego Star Wars: The Video Game
  - Windows: Inside the game directory, the default directory is at C:\Program Files\Giant\LEGO Star Wars Game
  - Mac: Sorry I don't know (I couldn't find a conclusive answer and feel free to let me know.)
- Lego Star Wars II: The Original Trilogy
  - Windows: C:\Users<Windows Username>\AppData\Local\LucasArts
  - Mac: ~/Library/Application Support/LucasArts/
- Lego Star Wars: The Complete Saga
  - Windows: C:\Users<Windows Username>\AppData\Local\LucasArts
  - Mac: ~/Library/Application Support/LucasArts/ or ~/Library/Application Support/Feral Interactive/LEGO Star Wars Saga/VFS/User/AppData/Roaming/LucasArts/ on later releases.
- Lego Indiana Jones: The Original Adventures
  - Windows: C:\Users<Windows Username>\AppData\Local\LucasArts
  - Mac: ~/Library/Preferences/Lucasarts/
- Lego Batman: The Video Game
  - Windows: C:\Users<Windows Username>\AppData\Local\Warner Bros. Interactive Entertainment
  - Mac: ~/Library/Preferences/Feral Interactive/Lego Batman/Saved Games/
- Lego Indiana Jones 2: The Adventure Continues
  - Windows: C:\Users<Windows Username>\AppData\Roaming\LucasArts
  - Mac: ~/Library/Application Support/Feral Interactive

I can't 100% confirm the directories for Mac since I don't currently have a Mac.

## Credits
This project is based on LSWSCU by Polly May.
The original concept, structure, and checksum logic come from that project, with extensions and adjustments added in this fork.

## License
This project is licensed under the GNU General Public License (GPL), in accordance with the original LSWSCU license.
You are free to use, modify, and distribute this software under the terms of the GPL.
Please credit the original author and do not claim the original work as your own.
