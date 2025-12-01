Downloads Organizer v1.0
Video Demo: <YOUR_YOUTUBE_LINK_HERE>



Description:

Downloads Organizer is a small app I built to help organize messy Downloads folders on a Mac. Downloads folders can get crowded over time with images, documents, videos, code files, and random downloads. I wanted something that could automatically sort files into categories but still give control, including the ability to undo any changes.

The project is written in Python using Tkinter for the interface. It’s designed to be easy to use: just a few clicks to organize a folder or undo the organization. The categories and file types are in a JSON file, which makes it easy to customize or add new categories without touching the code.




How It Works:

When a folder is selected, the app scans all the files. Each file’s extension is checked against the categories in categories.json. If a match is found, the file is moved into a folder with that category’s name. Examples:

.jpg, .jpeg, .png, .gif, .heic → Photos

.pdf, .docx, .txt → Documents

.mp4, .mov → Videos

Files that don’t match any category → Other

Screenshots are handled specially. If a filename contains “screenshot” or “screen shot,” it goes into a Screenshots subfolder inside Photos. This keeps screenshots separate from normal photos, since screenshots are usually for work, school, or tutorials.

The undo feature restores files to their original locations and removes empty category folders. This way, you can try the organizer without worrying about permanently changing your folders.




Project Files:

organizer.app – The standalone Mac app. You can double-click it to run, no setup needed.

organizer.py – The Python script with all the code for organizing files, handling screenshots, and undoing changes. This file was used to create the .app.

categories.json – The file that defines categories and the file types in each category. You can edit this to add or remove categories.



Design Decisions:

Screenshots in a Subfolder
I wanted screenshots separate from personal photos, so they are put in a Screenshots folder inside Photos. This makes it easier to find screenshots without digging through personal photos.

Undo Feature
Many apps permanently move files, which can be frustrating if it doesn’t work the way you expected. The undo button restores everything and removes empty folders, giving users confidence to try the app.

JSON Categories
Using a JSON file makes the app flexible. You can add a School folder for assignments or a Code folder for scripts without changing the code.

Simple GUI
Tkinter was chosen because it comes with Python and works on Mac without extra setup. The interface is simple, with buttons for organizing and undoing, so anyone can use it.

Easy to Use
Users select a folder, click organize, and the app does the rest. No confusing menus or settings.

Safe Undo
When undoing, files are checked for conflicts. If a file with the same name exists, _restored is added. This prevents overwriting or losing files.

Scalable Design
The app can be extended to include more file types, nested subfolders, or smarter sorting rules without major changes.




How to Run:

Double-click organizer.app to launch.

Click Organize Folder to select a folder to organize.

Click Undo Organization to revert any changes.

Keep categories.json in the same folder as the app so it knows how to sort files.




Future Improvements:

Allow custom category creation from the GUI.

Add support for Windows and Linux.

Drag-and-drop folder selection.

Smarter sorting by date, size, or other criteria.




Acknowledgments:

Python and Tkinter for making this project possible.

Personal inspiration from my own messy Downloads folder.