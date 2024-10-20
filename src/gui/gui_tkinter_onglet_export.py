import tkinter as tk
from tkinter import ttk

class ExportWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Exporter un Rapport")

        # Dimensions de la fenêtre
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)
        self.window.geometry(f"{window_width}x{window_height}")

        # Cadre pour l'exportation
        self.export_frame = ttk.Frame(self.window)
        self.export_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.export_frame, text="Exporter vos résultats")
        self.label.pack(pady=10)

        # Ajoutez ici les éléments pour l'exportation (ex: boutons, entrées)
