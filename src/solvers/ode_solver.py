import numpy as np
from .numerical_methods import NumericalMethods

class ODESolver:
    def __init__(self, equation, initial_conditions, method='euler_explicite', step_time=0.01):
        self.equation = equation
        self.initial_conditions = initial_conditions
        self.method = method
        self.numerical_methods = NumericalMethods(step_time=step_time)

    def solve(self, time_span):
        """Résoudre l'EDO avec la méthode spécifiée."""
        if self.method == 'euler_explicite':
            return self.numerical_methods.euler_explicite(self.equation, self.initial_conditions, time_span)
        elif self.method == 'euler_implicite':
            return self.numerical_methods.euler_implicite(self.equation, self.initial_conditions, time_span)
        else:
            raise ValueError(f"Méthode {self.method} non reconnue pour le solveur EDO.")

# Exemple d'utilisation
# def equation_example(y, t):
#     return np.array([-y[0] + t])

# solver = ODESolver(equation_example, [1], method='euler_explicite', step_time=0.1)
# results = solver.solve((0, 5))
# print(results)
