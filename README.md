Downloads Organizer


Youtube Link:
https://youtu.be/oF4VcIxnITY



Overview:

Downloads Organizer is a lightweight Python tool designed to help you quickly and efficiently organize the contents of your Downloads (or any folder) on macOS. With one click, the app categorizes your files into folders such as Photos, Documents, Videos, Audio, Code, and School, while keeping screenshots neatly tucked into a dedicated Screenshots subfolder.

The app also includes an Undo Organization feature, which restores files back to their original locations and removes any empty folders created during the organization process. The goal is to simplify file management without changing the way you work or requiring complicated setups.





Files in this Repository:

organizer.py – The main Python script. This file contains the GUI, the logic to organize files into categories, and the undo functionality.

categories.json – Defines which file extensions belong to which category. You can modify this file to add or remove file types or categories.

README.md – This file, explaining the project, design decisions, and usage.





How It Works:

Organize Folder: When you select a folder, the app scans all files, determines their type based on the categories.json file, and moves them into the appropriate folders. Screenshots are automatically placed into a Screenshots subfolder within Photos.

Undo Organization: If you don’t like the way files were organized, the app can reverse the process, moving files back to their original locations. Empty folders created during organization are also removed.

This design ensures your folder stays tidy while giving you the option to revert changes if needed.





Design Decisions:

GUI with Tkinter: Chosen for simplicity and cross-platform compatibility. The app can run locally on macOS without needing an external web browser or server.

JSON Configuration: Using categories.json allows for easy updates and customization without changing the Python code. Users can add new categories or file extensions quickly.

Undo Functionality: Implemented to respect users’ existing file organization. This way, if the automatic organization doesn’t match someone’s personal workflow, they can revert it immediately.

Screenshots Subfolder: Screenshots are handled differently because they often clutter the Photos folder. This small design choice helps keep image files organized intuitively.

One-Click Operation: The goal was to minimize user effort. You select a folder, click a button, and let the app do the work.






How to Run the App:

Make sure Python 3 is installed on your Mac.

Clone this repository or download the files.

Open Terminal, navigate to the repository folder, and run:

python3 organizer.py

A simple GUI will appear. Click Organize Folder to organize files, or Undo Organization to restore them.

Note: You do not need to install any packages manually if you’re running from the app bundled with PyInstaller. If running from Python source, you may need tkinter (which is pre-installed on most macOS Python distributions).





Future Improvements;

A fully standalone .app version that works out-of-the-box for anyone on macOS without running Python manually.

Additional customization options in the GUI for categories, folder names, and exceptions.

Integration with other operating systems like Windows or Linux.




Acknowledgements:

This project was inspired by the need for a clean, simple, and reversible file organization system. It was developed as a Harvard CS50 final project and reflects thoughtful consideration of usability and design choices.
