# VS Code-Cloner

Simple tool that allows to copy your current code written in VS Code into any other running application.

>Don't run duplicated terget applications or it will choose one 'randomly'.

**Warning: Currently it uses hotkey simulation. If something goes wrong it can delete anything on your computer, use it on your own risk.**

### Requirements:
- [Python](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
- [Run on Save extension](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save)

## Setup/usage

Change `targeted_app` to the desired window in the script.

In VS Code go to Settings **-->** Extensions **-->** Run on Save

Click on `Edit in settings.json` and paste the following:

```
"runOnSave.shell": "cmd.exe",
    "runOnSave.commands": [
        {
            "match": ".*\\.src",
            "command": "python Path/to/code_cloner.py < ${file}",
            "runIn": "backend"
        }
    ],
```
>Ensure that the path is correct, and match has been set up correctly (it uses regex search)

`Ctrl + Shift + P` **-->** `Run on Save: Enable`

Now when you save your current code it will be pasted in the targeted application.

The targeted app can be minimised, it will pop up automatically.

To see logs, open output in VS Code (`Ctrl + Shift + U`) and select `Run on Save` in the dropdown menu.

## Knowns issues
- If you use `Alt + Tab` to switch to the targeted application and your cursor is not automatically in the writable area (ie. you can't type), the script will not work.
- If there is an issue with the settings.json file, no error message will be displayed and the program won't execute. Log probably stays empty.