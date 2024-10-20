import tkinter as tk
from tkinter import ttk

class EquationFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Appel du constructeur de la classe parente

        self.configure(style="TFrame")

        # Label pour l'entrée de l'équation
        self.equation_label = tk.Label(self, text="Saisissez votre équation:", font=("Arial", 14))
        self.equation_label.grid(row=0, column=0, pady=10)

        # Champ d'entrée pour l'équation
        self.equation_entry = tk.Entry(self, width=40)
        self.equation_entry.grid(row=1, column=0, pady=10)

        # Bouton pour résoudre l'équation
        self.solve_button = tk.Button(self, text="Résoudre", command=self.solve_equation)
        self.solve_button.grid(row=2, column=0, pady=10)

        # Label pour afficher le résultat
        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, pady=10)

    def solve_equation(self):
        """Méthode pour résoudre l'équation (placeholder)."""
        equation = self.equation_entry.get()
        # Ajoutez ici votre logique pour résoudre l'équation
        # Exemple de résultat fictif
        result = f"Équation résolue: {equation}"
        self.result_label.config(text=result)
