import unittest
import numpy as np
from src.solvers.pde_solver import PDESolver

class TestPDESolver(unittest.TestCase):

    def test_crank_nicolson(self):
        def f(y, t):
            return np.array([-y[0]])

        solver = PDESolver(f, boundary_conditions=None, initial_conditions=lambda x: np.sin(np.pi * x), method='crank_nicolson', step_space=0.1, step_time=0.01)
        results = solver.solve((0, 1), (0, 1))
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
