#region Import Bibliotek I Danych
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox
import json
#endregion
#region Pobieranie Danych
def data_scrap(url_entry, label_data, file_path="Download_data.json"):
    
    # Pobranie Danych Z Strony
    url = url_entry.get().strip()
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        name = f"Dane Zostały Pobrane"
        label_data.config(text=name)
        label_data.grid()
    except requests.RequestException as e:
        return f"Błąd pobierania strony: {e}"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table")
    if not table:
        return "Nie znaleziono tabeli na stronie."
    # Przetwarzanie danych
    content = soup.find_all('tr')
    data = []
    
    for row in content:
        cells = row.find_all(['th', 'td'])
        text = [cell.get_text(strip=True) for cell in cells]
        if text:
            data.append(text)
    # Odczyt I Zapis Danych Do Pliku        
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)        
    print(f"Dane zostały pobrane z {url} i zapisane w pliku {file_path}")
#endregion
#region Okno Aplikacji
app2 = None 
def app2_window():
    global app2
    
    if app2 is not None and tk.Toplevel.winfo_exists(app2):
        messagebox.showerror("Błąd", "Okno pobierania jest już otwarte!")
        return
    
    app2 = tk.Toplevel()
    app2.resizable(False, False)
    app2.title("Pobieranie Danych")
    app2.geometry("400x600")
    app2.config(bg="white")
    app2.protocol("WM_DELETE_WINDOW", close_app)

    title_label = tk.Label(app2, text="Pobieranie Danych \n z Strony", bg="white", fg="#666", font=("Times New Roman", "24"))
    title_label.grid(row=0, column=0, pady=(100, 0), padx=(70, 30))
    
    name_label = tk.Label(app2, text="Podaj link do strony", bg="white", fg="#666", font=("Times New Roman", "14"))
    name_label.grid(row=1, column=0, pady=(20, 0), padx=(70, 30))
    
    url_entry = tk.Entry(app2, width=30, bg="orange", fg="white", font=("Times New Roman", 14))
    url_entry.grid(row=2, column=0, pady=(20, 0), padx=(60, 30))

    data_dwn = tk.Button(app2, text="Pobierz dane", bg="orange", fg="white", font=("Times New Roman", 14), command=lambda: data_scrap(url_entry, label_data))
    data_dwn.grid(row=3, column=0, pady=(20, 0), padx=(70, 30))
    label_data = tk.Label(app2, text="", bg="white", fg="#666", font=("Times New Roman", "14"))
    label_data.grid(row=4, column=0, pady=(5, 0), padx=(70, 30))
    label_data.grid_remove()
    
    app2_close = tk.Button(app2, text="Powrót", bg="orange", fg="white", font=("Times New Roman", 14), command=close_app)
    app2_close.grid(row=5, column=0, pady=(20, 0), padx=(70, 30))   
#endregion
#region Czyszczenie pliku JSON
def data_dump(file_path="Download_data.json"):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)
#endregion
#region Zamykanie Okna
def close_app():
    global app2
    if app2 is not None:
        app2.destroy()
        app2 = None
#endregion