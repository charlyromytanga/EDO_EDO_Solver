import numpy as np

class NumericalMethods:
    def __init__(self, step_size=0.01, step_time=0.01, method="Euler", params=None):
        self.step_size = step_size
        self.step_time = step_time
        self.method = method
        self.params = params if params else {}
        self.initial_conditions = []

    def discretize_space(self, space_range):
        """Discrétise l'espace en fonction de step_size."""
        start, end = space_range
        return [start + i * self.step_size for i in range(int((end - start) / self.step_size) + 1)]

    def discretize_time(self, time_range):
        """Discrétise le temps en fonction de step_time."""
        start, end = time_range
        return [start + i * self.step_time for i in range(int((end - start) / self.step_time) + 1)]

    def euler_explicite(self, f, y0, time_span):
        """Méthode d'Euler explicite pour résoudre les EDO : dy/dt = f(y, t)."""
        time_points = self.discretize_time(time_span)
        y = np.array(y0)
        results = [y.copy()]

        for t in time_points[1:]:
            y += self.step_time * f(y, t)
            results.append(y.copy())

        return results

    def euler_implicite(self, f, y0, time_span, tol=1e-5, max_iter=100):
        """Méthode d'Euler implicite pour résoudre les EDO, utilisant la méthode de Newton."""
        def newton_raphson(g, dg, y_guess):
            """Méthode de Newton-Raphson pour trouver y(n+1)."""
            for _ in range(max_iter):
                y_new = y_guess - np.linalg.solve(dg(y_guess), g(y_guess))
                if np.linalg.norm(y_new - y_guess) < tol:
                    return y_new
                y_guess = y_new
            raise ValueError("Méthode de Newton n'a pas convergé.")

        time_points = self.discretize_time(time_span)
        y = np.array(y0)
        results = [y.copy()]

        for t in time_points[1:]:
            # Définir la fonction g et sa dérivée dg pour Newton-Raphson
            g = lambda ynp1: ynp1 - y - self.step_time * f(ynp1, t + self.step_time)
            dg = lambda ynp1: np.eye(len(y)) - self.step_time * self.jacobian(f, ynp1, t + self.step_time)
            
            y_next = newton_raphson(g, dg, y)
            y = y_next
            results.append(y.copy())

        return results

    def jacobian(self, f, y, t):
        """Estime la jacobienne df/dy pour la méthode de Newton (approximation par différences finies)."""
        n = len(y)
        jacobian = np.zeros((n, n))
        delta = 1e-6
        for i in range(n):
            y_delta = y.copy()
            y_delta[i] += delta
            jacobian[:, i] = (f(y_delta, t) - f(y, t)) / delta
        return jacobian

# Exemple d'utilisation :
# def f_example(y, t):
#     return np.array([-y[0] + t])

# nm = NumericalMethods(step_size=0.1, step_time=0.1)
# results_explicit = nm.euler_explicite(f_example, [1], (0, 5))
# results_implicit = nm.euler_implicite(f_example, [1], (0, 5))
# print(results_explicit)
# print(results_implicit)
