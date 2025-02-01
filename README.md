<div align="center">

# 🗓️ Class Schedule Generator 🕑
Simple scheduling tool for school/college classes written in Python, using PySide6 Libraries.
![imagen](https://github.com/user-attachments/assets/fd3d720d-1a5f-4c5a-be07-00eba6d32a07)

</div>

## Why
I always make my college class schedule in my phone's calendar, pretty slow task, even when it's done once a period, that's why i've written this program, to simplify somewhat the process, that's all.
## How
I made this program in Python, to use the less as possible of additional libraries (The only requirement is Pyside6). The standard filetipe for calendars and scheduling is iCalendar (extension .ics), a plain text file containing data of events and alerts including Time Zone information and others, these files are readable by most (if not all) calendar programs and web apps. The program generates this file based on the settings on the program.
## Installation
**Precompiled binaries doesn't require installation**, but you can run the program from the source, the only requirement (in addition of the Python interpreter) is `Pyside6` libraries installed on your system, you can install them by running this command on CMD (Windows) or a Python Venv (Linux / MacOS)
```sh
    pip install Pyside6
```
And then, execute `src/main.py` using the Python interpreter
```sh
    python src/main.py
```
## Usage
Simply add the classes you'd like, set your class period settings (Start-End) and customize as you like the calendar, you can always save your progress to a text file clicking `Save`. Once you're done with your changes, click `Export to .ics file`, select where you want the file and save. Most popular .ics clients (E.G. Google Calendar, Microsoft Outlook) will let you import the file.
## Bug reporting / Feature requests / Contributing
All Issues or Pull requests are welcome.
