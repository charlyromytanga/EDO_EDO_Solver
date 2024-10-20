import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class VisualizationFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Créer une figure Matplotlib pour la visualisation
        self.figure = plt.Figure(figsize=(8, 6))
        self.ax = self.figure.add_subplot(111, projection='3d')

        # Appeler la méthode pour dessiner la surface de l'équation de la chaleur
        self.draw_heat_equation_surface()

        # Créer un canevas pour afficher la figure
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def draw_heat_equation_surface(self):
        """Dessine la surface de solution de l'équation de la chaleur."""
        # Définir le domaine
        x = np.linspace(0, 5, 100)
        y = np.linspace(0, 5, 100)
        X, Y = np.meshgrid(x, y)

        # Calculer la solution de l'équation de la chaleur (exemple simplifié)
        Z = np.sin(np.pi * X) * np.sin(np.pi * Y) * np.exp(-0.1 * (X**2 + Y**2))

        # Dessiner la surface
        self.ax.plot_surface(X, Y, Z, cmap='viridis')

        # Ajouter des étiquettes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Temperature')
        self.ax.set_title('Surface de la solution de l\'équation de la chaleur')

        # Améliorer l'affichage
        self.ax.view_init(elev=30, azim=30)  # Angles de vue
