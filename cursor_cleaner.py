import os
import shutil
import tkinter as tk
from tkinter import messagebox

APPDATA = os.getenv("APPDATA")
LOCALAPPDATA = os.getenv("LOCALAPPDATA")

PATHS_TO_DELETE = [
    os.path.join(APPDATA, "Cursor"),
    os.path.join(LOCALAPPDATA, "Cursor"),
]

def delete_path(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            return True
        return False
    except Exception as e:
        return str(e)

def clean_cursor():
    results = []
    for path in PATHS_TO_DELETE:
        result = delete_path(path)
        results.append((path, result))

    msg = ""
    for path, res in results:
        if res is True:
            msg += f"✔ O‘chirildi: {path}\n"
        elif res is False:
            msg += f"ℹ Topilmadi: {path}\n"
        else:
            msg += f"❌ Xatolik: {path}\n{res}\n"

    msg += "\nCursor tozalandi.\nDasturga qayta kirishda login so‘raladi."
    messagebox.showinfo("Cursor Cleaner", msg)

# UI
root = tk.Tk()
root.title("Cursor AI Cleaner")
root.geometry("420x220")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Cursor AI kesh va login ma'lumotlarini\no‘chirish",
    font=("Segoe UI", 11),
    pady=20
)
label.pack()

btn = tk.Button(
    root,
    text="🧹 Tozalash (Sign out)",
    font=("Segoe UI", 11),
    width=25,
    height=2,
    command=clean_cursor
)
btn.pack(pady=10)

note = tk.Label(
    root,
    text="⚠ Cursor yopiq bo‘lishi kerak!",
    fg="red"
)
note.pack()

root.mainloop()
