#region Import Bibliotek I Danych
import tkinter as tk
from tkinter import *
import Data_download
import Data_pars
import Data_display
#endregion
#region Główne Okno
# Główne Okno Aplikacji
app = tk.Tk()
app.resizable(False, False)
app.title("Aplikacja UI/UX")
app.geometry("400x600")
app.config(bg="white")

# Tytuł
title_label = tk.Label(app, text="Prosta Aplikacja \n Indeksowania Stron", bg="white", fg="#666", font=("Times New Roman", "24"))
title_label.grid(row=0, column=0, pady=(100, 0), padx=(70, 30))
#endregion
#region Komunikaty
# Pobieranie
def dwn_show():
    Data_download.app2_window()
    name = f"Operacja Przeprowadzana \n w Nowym Oknie"
    label_data.config(text=name)
    label_data.grid()
    label_pars.grid_remove()
    label_display.grid_remove()
    label_dump.grid_remove()
# Parsowanie
def pars_show():
    Data_pars.pars_file()
    label_pars.config(text="Dane Zostały Przeanalizowane")
    label_pars.grid()
    label_data.grid_remove()
    label_display.grid_remove()
    label_dump.grid_remove()
# Wyświetlanie
def display_show():
    Data_display.display_data()
    label_display.config(text="Dane Są Wyświetlane \n W Nowym Oknie")
    label_display.grid()
    label_data.grid_remove()
    label_pars.grid_remove()
    label_dump.grid_remove()
# Usuwanie
def dump_show():
    Data_download.data_dump()
    label_dump.config(text="Dane Zostały Usunięte")
    label_dump.grid()
    label_data.grid_remove()
    label_pars.grid_remove()
    label_display.grid_remove()
#endregion
#region Pobieranie Danych
data_dwn = tk.Button(app, text="Pobieranie Danych", bg="orange", fg="White", font=("14"), command=dwn_show)
data_dwn.grid(row=1, column=0, pady=(20, 0), padx=(70, 30))
label_data = tk.Label(app, text="", bg="white", fg="#666", font=("Times New Roman", "14"))
label_data.grid(row=2, column=0, pady=(5, 0), padx=(70, 30))
label_data.grid_remove()
#endregion
#region Parsowanie Danych
data_pars = tk.Button(app, text="Parsowanie Danych", bg="orange", fg="White", font=("14"), command=pars_show)
data_pars.grid(row=3, column=0, pady=(20, 0), padx=(70, 30))
label_pars = tk.Label(app, text="", bg="white", fg="#666", font=("Times New Roman", "14"))
label_pars.grid(row=4, column=0, pady=(5, 0), padx=(70, 30))
label_pars.grid_remove()
#endregion
#region Wyświetlanie W App
display_data = tk.Button(app, text="Wyświetl Dane", bg="orange", fg="White", font=("14"), command=display_show)
display_data.grid(row=5, column=0, pady=(20, 0), padx=(70, 30))
label_display = tk.Label(app, text="", bg="white", fg="#666", font=("Times New Roman", "14"))
label_display.grid(row=6, column=0, pady=(5, 0), padx=(70, 30))
label_display.grid_remove()
#endregion
#region Usuwanie Danych
dump_data = tk.Button(app, text="Usuń Dane", bg="orange", fg="White", font=("14"), command=dump_show)
dump_data.grid(row=7, column=0, pady=(20, 0), padx=(70, 30))
label_dump = tk.Label(app, text="", bg="white", fg="#666", font=("Times New Roman", "14"))
label_dump.grid(row=8, column=0, pady=(5, 0), padx=(70, 30))
label_dump.grid_remove()
#endregion
#region Zamykanie Aplikacji
# Funkcja do zamknięcia aplikacji
def close_app():
    Data_download.data_dump()
    app.destroy()
 
# Przycisk do wyjścia
close_app = tk.Button(app, text="Wyjście", bg="orange", fg="White", font=("14"), command=close_app)
close_app.grid(row=9, column=0, pady=(20, 0), padx=(70, 30))
#endregion
#region Uruchomienie aplikacji
app.mainloop()
#endregion