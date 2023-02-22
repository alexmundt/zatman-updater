# Zatman Updater
This tool updates the HTML website for the SEDI webpage.

# Usage
To use the tool run 
``` 
python GUI.png
```

# Dependencies
Uses 
- tkinter
- os
- configparser

from the standard library.

Also uses 
- pandas

# Compilation instructions
Can be compiled to exe with the following pyinstaller command.
```
pyinstaller -i "gui.ico" --noconsole --onefile --add-data "gui.png;." GUI.py
```
## Note:
- [ ] upload "gui.ico" from the distributabe folder
