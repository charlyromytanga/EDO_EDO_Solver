import unittest
import numpy as np
from src.visualization.plot_results import PlotResults

class TestPlotResults(unittest.TestCase):

    def test_plot_2d(self):
        """Tester la génération d'un graphique 2D."""
        x_data = np.linspace(0, 10, 100)
        y_data = np.sin(x_data)
        plotter = PlotResults(title="Test Plot 2D", labels={"x_label": "X", "y_label": "Sin(X)"})
        try:
            plotter.plot_2d(x_data, y_data)
        except Exception as e:
            self.fail(f"plot_2d failed with exception: {e}")

    def test_plot_3d(self):
        """Tester la génération d'un graphique 3D."""
        x_data = np.linspace(0, 10, 50)
        y_data = np.linspace(0, 10, 50)
        X, Y = np.meshgrid(x_data, y_data)
        Z = np.sin(np.sqrt(X**2 + Y**2))
        plotter = PlotResults(title="Test Plot 3D", labels={"x_label": "X", "y_label": "Y", "z_label": "Z"})
        try:
            plotter.plot_3d(x_data, y_data, Z)
        except Exception as e:
            self.fail(f"plot_3d failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
