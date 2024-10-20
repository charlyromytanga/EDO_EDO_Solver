import unittest
import numpy as np
from src.solvers.ode_solver import ODESolver

class TestODESolver(unittest.TestCase):

    def test_euler_explicite(self):
        def f(y, t):
            return np.array([-y[0]])
        
        solver = ODESolver(f, [1], method='euler_explicite', step_time=0.1)
        results = solver.solve((0, 1))
        expected = [1 * (0.9 ** i) for i in range(len(results))]
        np.testing.assert_almost_equal([r[0] for r in results], expected, decimal=2)

    def test_euler_implicite(self):
        def f(y, t):
            return np.array([-y[0]])
        
        solver = ODESolver(f, [1], method='euler_implicite', step_time=0.1)
        results = solver.solve((0, 1))
        expected = [1 * (0.9 ** i) for i in range(len(results))]
        np.testing.assert_almost_equal([r[0] for r in results], expected, decimal=2)

if __name__ == '__main__':
    unittest.main()
