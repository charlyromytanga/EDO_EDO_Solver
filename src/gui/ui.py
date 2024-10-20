import tkinter as tk

class EquationInputParser:
    def __init__(self, equation_entry, lower_bound_entry, upper_bound_entry):
        self.equation_entry = equation_entry
        self.lower_bound_entry = lower_bound_entry
        self.upper_bound_entry = upper_bound_entry

    def insert_symbol(self, symbol):
        """Insérer un symbole dans le champ de saisie de l'équation."""
        current_position = self.equation_entry.index(tk.INSERT)
        self.equation_entry.insert(current_position, symbol)
        self.equation_entry.focus()

    def insert_derivative(self, symbol):
        """Insérer un symbole de dérivée dans le champ de saisie de l'équation."""
        current_position = self.equation_entry.index(tk.INSERT)
        self.equation_entry.insert(current_position, f"{symbol}(")
        self.equation_entry.focus()

    def insert_integral(self):
        """Insérer un symbole d'intégrale dans le champ de saisie de l'équation."""
        current_position = self.equation_entry.index(tk.INSERT)
        self.equation_entry.insert(current_position, f"∫[{self.lower_bound_entry.get()}] [{self.upper_bound_entry.get()}]")
        self.equation_entry.focus()
