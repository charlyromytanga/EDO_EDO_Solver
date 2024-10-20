import tkinter as tk
from tkinter import ttk

class ParametersWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Paramètres")
        
        # Dimensions de la fenêtre
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)
        self.window.geometry(f"{window_width}x{window_height}")

        # Cadre pour les paramètres
        self.parameters_frame = ttk.Frame(self.window)
        self.parameters_frame.pack(fill=tk.BOTH, expand=True)

        # Ajoutez ici les éléments pour les paramètres (ex: entrées, labels)
        self.label = tk.Label(self.parameters_frame, text="Paramètres de l'équation")
        self.label.pack(pady=10)
