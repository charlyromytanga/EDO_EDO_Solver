from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from solvers.edo_solver import solve_edo  # Appel à ton module de résolution des EDO
from solvers.edp_solver import solve_edp  # Appel à ton module de résolution des EDP

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        domain = request.form['domain']
        equation = request.form['equation']
        constants = request.form['constants']
        time_interval = list(map(float, request.form['time_interval'].split(',')))
        time_step = float(request.form['time_step'])

        if domain == "EDO":
            t, solution = solve_edo(equation, constants, time_interval, time_step)
            fig, ax = plt.subplots()
            ax.plot(t, solution)
            ax.set_title('Solution EDO')
        elif domain == "EDP":
            space_interval = list(map(float, request.form['space_interval'].split(',')))
            space_step = float(request.form['space_step'])
            X, T, solution = solve_edp(equation, constants, time_interval, time_step, space_interval, space_step)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, T, solution, cmap='viridis')
            ax.set_title('Solution EDP')

        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('index.html', plot_url=plot_url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
