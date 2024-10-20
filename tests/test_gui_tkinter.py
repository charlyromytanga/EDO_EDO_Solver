import tkinter as tk
from tkinter import ttk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gui.gui_tkinter import *
print("chemin dans sys.path :", sys.path)

# Fonction de simulation pour résoudre une EDO (pour le test)
def fake_solve_edo(equation, constants, time_interval, time_step):
    print(f"Résolution EDO simulée pour l'équation: {equation}, constantes: {constants}")
    return list(range(int(time_interval[0]), int(time_interval[1]), int(time_step))), [1, 2, 3, 4, 5]

# Fonction pour gérer la résolution (simulée) et affichage dans Tkinter
def solve_and_plot():
    domain = domain_var.get()
    equation = equation_entry.get()
    constants = constants_entry.get()
    time_interval = list(map(float, time_interval_entry.get().split(',')))
    time_step = float(time_step_entry.get())

    if domain == "EDO":
        t, solution = fake_solve_edo(equation, constants, time_interval, time_step)
        print(f"Résultat de l'EDO: {solution}")
    else:
        print("Pas encore implémenté pour EDP")

# Création de l'interface Tkinter
window = tk.Tk()
window.title("Test d'utilisation Tkinter")

# Widgets pour les entrées utilisateur
tk.Label(window, text="Domaine :").pack()
domain_var = tk.StringVar(value="EDO")
ttk.Combobox(window, textvariable=domain_var, values=["EDO", "EDP"]).pack()

tk.Label(window, text="Equation :").pack()
equation_entry = tk.Entry(window)
equation_entry.pack()

tk.Label(window, text="Constantes :").pack()
constants_entry = tk.Entry(window)
constants_entry.pack()

tk.Label(window, text="Intervalle de temps :").pack()
time_interval_entry = tk.Entry(window)
time_interval_entry.pack()

tk.Label(window, text="Pas temporel :").pack()
time_step_entry = tk.Entry(window)
time_step_entry.pack()

# Bouton pour lancer la résolution
tk.Button(window, text="Résoudre", command=solve_and_plot).pack()

# Lancement de l'interface Tkinter
window.mainloop()
