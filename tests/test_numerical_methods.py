import unittest
import numpy as np
from src.solvers.numerical_methods import NumericalMethods

class TestNumericalMethods(unittest.TestCase):

    def setUp(self):
        self.nm = NumericalMethods(step_size=0.1, step_time=0.1)
    
    def test_discretize_space(self):
        space_points = self.nm.discretize_space((0, 1))
        expected_points = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.assertEqual(space_points, expected_points)

    def test_discretize_time(self):
        time_points = self.nm.discretize_time((0, 1))
        expected_points = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.assertEqual(time_points, expected_points)
    
    def test_euler_explicite(self):
        def f(y, t):
            return np.array([-y[0]])

        results = self.nm.euler_explicite(f, [1], (0, 1))
        expected = [1 * (0.9 ** i) for i in range(len(results))]
        np.testing.assert_almost_equal([r[0] for r in results], expected, decimal=2)
    
    def test_euler_implicite(self):
        def f(y, t):
            return np.array([-y[0]])

        results = self.nm.euler_implicite(f, [1], (0, 1))
        expected = [1 * (0.9 ** i) for i in range(len(results))]
        np.testing.assert_almost_equal([r[0] for r in results], expected, decimal=2)

if __name__ == '__main__':
    unittest.main()
