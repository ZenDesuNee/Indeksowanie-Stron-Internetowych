#region Import Bibliotek I Danych
import tkinter as tk
from tkinter import ttk, messagebox
import json
#endregion
#region Wyświetlanie Danych
app3 = None
def display_data(file_path="Download_data.json"):
    global app3
    
    if app3 is not None and tk.Toplevel.winfo_exists(app3):
        messagebox.showerror("Błąd", "Okno z danymi jest już otwarte!")
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except json.JSONDecodeError:
        return "Plik Json Jest Pusty/Nieprawidłowy"
    
    headers = existing_data[0]
    data_rows = existing_data[1:]
    
    app3 = tk.Toplevel()
    app3.resizable(False, False)
    app3.title("Przeanalizowane Dane")
    app3.geometry("1000x600")
    app3.config(bg="white")
    app3.protocol("WM_DELETE_WINDOW", lambda: close_app())
    
    label = tk.Label(app3, text="Tablica Drużyn Hokejowych W latach 90", bg="white", fg="#666", font=("Times New Roman", "24"))
    label.pack(pady=(10, 5))
    
    tree = ttk.Treeview(app3, columns=headers, show="headings")
    tree.pack(expand=True, fill="both", padx=20, pady=20)

    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    for row in data_rows:
        tree.insert("", "end", values=row)

    close_button = tk.Button(app3, text="Zamknij", command=close_app, bg="orange", fg="White")
    close_button.pack(pady=(0, 20))
#endregion
#region Zamykanie Okna
def close_app():
    global app3
    if app3 is not None:
        app3.destroy()
        app3 = None
#endregion