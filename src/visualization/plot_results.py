import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class PlotResults:
    def __init__(self, title="Graph", labels=None):
        self.title = title
        self.labels = labels if labels else {"x_label": "X", "y_label": "Y", "z_label": "Z"}

    def plot_2d(self, x_data, y_data, line_style='-', color='blue'):
        """Tracer un graphique 2D."""
        plt.figure(figsize=(8, 6))
        plt.plot(x_data, y_data, line_style, color=color)
        plt.xlabel(self.labels.get("x_label", "X"))
        plt.ylabel(self.labels.get("y_label", "Y"))
        plt.title(self.title)
        plt.grid(True)
        plt.show()

    def plot_3d(self, x_data, y_data, z_data, color='blue'):
        """Tracer un graphique 3D."""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(x_data, y_data)
        ax.plot_surface(X, Y, z_data, color=color)
        ax.set_xlabel(self.labels.get("x_label", "X"))
        ax.set_ylabel(self.labels.get("y_label", "Y"))
        ax.set_zlabel(self.labels.get("z_label", "Z"))
        ax.set_title(self.title)
        plt.show()
