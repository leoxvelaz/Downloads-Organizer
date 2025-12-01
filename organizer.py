import os
import shutil
import json
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# ------------------------------
# Load categories from JSON file
# ------------------------------
def load_categories(json_filename="categories.json"):
    try:
        if getattr(sys, "frozen", False):
            # Running as PyInstaller app
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        json_path = os.path.join(base_path, json_filename)

        with open(json_path, "r") as f:
            data = json.load(f)

        return data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load categories:\n{e}")
        return {}

# ---------------------------------
# Organize files based on categories
# ---------------------------------
def organize_folder(folder_path, categories):
    moved_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            # Find matching category
            matched_category = None
            for category, extensions in categories.items():
                if file_ext in extensions:
                    matched_category = category
                    break

            if matched_category:
                category_folder = os.path.join(folder_path, matched_category)

                # Create main category folder if missing
                os.makedirs(category_folder, exist_ok=True)

                # Special rule: screenshots inside Photos
                if matched_category.lower() in ["images", "photos"]:
                    if "screenshot" in filename.lower() or "screen shot" in filename.lower():
                        screenshot_folder = os.path.join(category_folder, "Screenshots")
                        os.makedirs(screenshot_folder, exist_ok=True)
                        dest = os.path.join(screenshot_folder, filename)
                    else:
                        dest = os.path.join(category_folder, filename)
                else:
                    dest = os.path.join(category_folder, filename)

                try:
                    shutil.move(file_path, dest)
                    moved_files.append(filename)
                except Exception as e:
                    print(f"Failed to move {filename}: {e}")

    return moved_files

# ------------------------------------
# Undo organization
# ------------------------------------
def undo_organization(folder_path):
    restored = []

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for filename in files:
            src = os.path.join(root, filename)
            dest = os.path.join(folder_path, filename)

            # Avoid overwriting
            if os.path.exists(dest):
                base, ext = os.path.splitext(filename)
                counter = 1
                new_name = f"{base}_restored{ext}"
                new_dest = os.path.join(folder_path, new_name)

                while os.path.exists(new_dest):
                    counter += 1
                    new_name = f"{base}_restored{counter}{ext}"
                    new_dest = os.path.join(folder_path, new_name)

                dest = new_dest

            try:
                shutil.move(src, dest)
                restored.append(os.path.basename(dest))
            except Exception as e:
                print(f"Undo failed for {src}: {e}")

        # Remove empty directories
        for d in dirs:
            dir_path = os.path.join(root, d)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass

    # Clean up top-level category folders if empty
    for item in os.listdir(folder_path):
        path = os.path.join(folder_path, item)
        if os.path.isdir(path):
            try:
                os.rmdir(path)
            except OSError:
                pass

    return restored

# -------------------------
# GUI Button Functionality
# -------------------------
def select_folder_for_organize():
    folder = filedialog.askdirectory()
    if not folder:
        return

    categories = load_categories()
    moved = organize_folder(folder, categories)

    if moved:
        messagebox.showinfo("Success", f"Organized {len(moved)} files.")
    else:
        messagebox.showinfo("Info", "No files were organized.")

def select_folder_for_undo():
    folder = filedialog.askdirectory()
    if not folder:
        return

    restored = undo_organization(folder)

    if restored:
        messagebox.showinfo("Success", f"Restored {len(restored)} files.")
    else:
        messagebox.showinfo("Info", "No files needed to be restored.")

# ---- GUI Setup ----
root = tk.Tk()
root.title("Downloads Organizer")
root.geometry("420x250")

title = tk.Label(root, text="Downloads Organizer", font=("Arial", 18))
title.pack(pady=15)

organize_btn = tk.Button(root, text="Organize Folder", font=("Arial", 14),
                         command=select_folder_for_organize, width=20)
organize_btn.pack(pady=10)

undo_btn = tk.Button(root, text="Undo Organization", font=("Arial", 14),
                     command=select_folder_for_undo, width=20)
undo_btn.pack(pady=10)

footer = tk.Label(root, text="Designed by Leo", font=("Arial", 11))
footer.pack(side="bottom", pady=10)

root.mainloop()
