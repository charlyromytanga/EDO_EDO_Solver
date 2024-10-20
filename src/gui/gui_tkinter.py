import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

from .gui_tkinter_onglet_parameters import ParametersWindow
from .gui_tkinter_onglet_visualisation import VisualizationFrame
from .gui_tkinter_onglet_export import ExportWindow
from .gui_tkinter_onglet_equation import EquationFrame  # Importez la nouvelle classe



class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Résolveur d'Équations")
        self.root.geometry("1920x1080")  # Prendre toute la taille de l'écran

        # Style de la fenêtre
        style = ttk.Style()
        style.configure("TFrame", background="#B0E0E6")  # Teinte de bleu clair

        # Créer la barre de menu
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Sous-menu pour Résolution
        equation_menu = tk.Menu(self.menu_bar, tearoff=0)
        equation_menu.add_command(label="Lancer la résolution", command=self.open_equation_window)
        self.menu_bar.add_cascade(label="Résolution", menu=equation_menu)

        # Sous-menu pour Les schémas
        parameters_menu = tk.Menu(self.menu_bar, tearoff=0)
        parameters_menu.add_command(label="Choisir un schéma", command=self.open_parameters_window)
        self.menu_bar.add_cascade(label="Les schémas", menu=parameters_menu)

        # Sous-menu pour la Visualisation
        visualization_menu = tk.Menu(self.menu_bar, tearoff=0)
        visualization_menu.add_command(label="Visualiser Surface", command=self.show_default_visualization)
        self.menu_bar.add_cascade(label="Visualisation", menu=visualization_menu)

        # Sous-menu pour l'Exportation
        export_menu = tk.Menu(self.menu_bar, tearoff=0)
        export_menu.add_command(label="Exporter en PDF (FR)", command=lambda: self.export_report("fr"))
        export_menu.add_command(label="Exporter en PDF (EN)", command=lambda: self.export_report("en"))
        self.menu_bar.add_cascade(label="Exporter un Rapport", menu=export_menu)

        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Diviser la fenêtre principale en deux parties
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Séparer les parties par un trait noir
        self.separator = ttk.Separator(self.main_frame, orient='vertical')
        self.separator.pack(side=tk.LEFT, fill=tk.Y)


        # Sections de la partie gauche
        # Section haute
        self.top_left_frame = ttk.Frame(self.left_frame)
        self.top_left_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configuration supplémentaire pour que `left_frame` prenne tout l'espace disponible
        self.left_frame.grid_columnconfigure(0, weight=1)

        # Ajouter des contenus interactifs
        self.create_left_section_content()

        # Section droite (affichage de la surface des solutions)
        self.visualization_frame = ttk.Frame(self.right_frame)
        self.visualization_frame.pack(fill=tk.BOTH, expand=True)

        # Afficher un message d'accueil dans la partie haute gauche
        self.main_label = tk.Label(self.top_left_frame, text="", background="#B0E0E6", font=("Arial", 14))
        self.main_label.pack(pady=20)

        # Visualisation par défaut de l'actif financier
        self.show_default_visualization()

        # Configuration de  la saisie d'équations
        self.equation_input_frame = ttk.Frame(self.top_left_frame)
        self.equation_input_frame.pack(fill=tk.X, padx=5, pady=5)
        

        # Configuration pour le nombre d'équations
        self.setup_equation_input_section()

    def setup_equation_input_section(self):
        """Configurer la saisie des équations."""
        # Label pour le nombre d'équations
        num_eq_label_1 = ttk.Label(self.equation_input_frame, text="Nombre d'équations du problèmes :", font=("Arial", 10))
        num_eq_label_1.grid(row=2, column=0, sticky=tk.W, padx=5)

        num_eq_label_2 = ttk.Label(self.equation_input_frame, text="Nombre d'équations des conditions :", font=("Arial", 10))
        num_eq_label_2.grid(row=2, column=2, sticky=tk.W, padx=5)

        # Spinbox pour définir le nombre d'équations
        self.num_equations_spinbox = tk.Spinbox(self.equation_input_frame, from_=1, to=10, command=self.update_equation_fields)
        self.num_equations_spinbox.grid(row=2, column=1, padx=5)

        # Bouton pour générer les champs de saisie
        generate_button = ttk.Button(self.equation_input_frame, text="Générer", command=self.update_equation_fields)
        generate_button.grid(row=2, column=2, padx=5)

        # Frame pour les champs d'équations
        self.equation_fields_frame = ttk.Frame(self.equation_input_frame)
        self.equation_fields_frame.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # Mettre à jour les champs de saisie initialement
        self.update_equation_fields()

    def update_equation_fields(self):
        """Mettre à jour le nombre de champs de saisie d'équations basé sur le nombre sélectionné."""
        # Effacer les champs existants
        for widget in self.equation_fields_frame.winfo_children():
            widget.destroy()

        num_equations = int(self.num_equations_spinbox.get())
        for i in range(num_equations):
            frame = ttk.Frame(self.equation_fields_frame)
            frame.pack(pady=5, fill=tk.X)

            label = ttk.Label(frame, text=f"Équation {i + 1} :")
            label.pack(side=tk.TOP, padx=5)

            equation_entry = tk.Text(frame, height=1, width=30)
            equation_entry.pack(side=tk.TOP, padx=5)

        # Créer un frame pour centrer les boutons
        button_frame = ttk.Frame(frame)
        button_frame.pack(side=tk.TOP, pady=5)  # Ajouter le cadre de boutons sous le champ de saisie

        # Bouton de validation
        validate_btn = ttk.Button(button_frame, text="Valider", command=lambda eq=equation_entry: self.validate_equation(eq))
        validate_btn.pack(side=tk.LEFT, padx=5)  # Sur la même ligne

        # Bouton d'effacement
        clear_btn = ttk.Button(button_frame, text="Effacer", command=lambda eq=equation_entry: self.clear_equation(eq))
        clear_btn.pack(side=tk.LEFT, padx=5)  # Sur la même ligne

    def validate_equation(self, equation_text_widget):
        """Valider l'équation saisie et afficher un message."""
        equation = equation_text_widget.get("1.0", tk.END).strip()
        if not equation:
            messagebox.showerror("Erreur", "L'équation ne peut pas être vide.")
            return
        print(f"Équation validée : {equation}")

    def clear_equation(self, equation_text_widget):
        """Effacer le contenu de l'équation saisie."""
        equation_text_widget.delete("1.0", tk.END)



    def validate_real_number_input(self, value):
        """Validation pour n'accepter que les valeurs réelles (nombres positifs ou négatifs avec décimales)."""
        if value == "" or value == "-":
            return True  # Accepter l'entrée vide ou juste un tiret pour permettre la saisie de nombres négatifs
        
        try:
            float(value)  # Essayer de convertir la saisie en un nombre réel
            return True
        except ValueError:
            return False

    def on_validate_param1(self):
        """Fonction pour valider et utiliser la valeur de Paramètre 1"""
        param1_value = self.entry_param1.get()
        try:
            param1_value = float(param1_value)  # Convertir en valeur réelle
            print(f"Paramètre 1 validé avec la valeur : {param1_value}")
            # Ajoutez ici les actions à effectuer avec la valeur validée
        except ValueError:
            print("Erreur : Veuillez entrer une valeur réelle valide pour Paramètre 1.")

    def on_validate_param2(self):
        """Fonction pour valider et utiliser la valeur de Paramètre 2"""
        param2_value = self.entry_param2.get()
        try:
            param2_value = float(param2_value)  # Convertir en valeur réelle
            print(f"Paramètre 2 validé avec la valeur : {param2_value}")
            # Ajoutez ici les actions à effectuer avec la valeur validée
        except ValueError:
            print("Erreur : Veuillez entrer une valeur réelle valide pour Paramètre 2.")


    def create_left_section_content(self):
        """Ajouter des boutons radio et des champs de saisie en deux colonnes dans chaque section gauche."""
        # Variables pour les boutons radio
        self.radio_var_type_left = tk.StringVar(value="EDO")
        self.radio_var_regular_left = tk.StringVar(value="Linéaire")
        
        # Organiser les boutons radio
        top_options_frame = ttk.Frame(self.top_left_frame)
        top_options_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        # (EDO/EDP)
        butoton_radio_type_left_frame = ttk.Frame(top_options_frame)
        butoton_radio_type_left_frame.grid(row=0, column=0, sticky=tk.W, padx=5)
        tk.Radiobutton(butoton_radio_type_left_frame, text="EDO", variable=self.radio_var_type_left, value="EDO").pack(anchor=tk.W)
        tk.Radiobutton(butoton_radio_type_left_frame, text="EDP", variable=self.radio_var_type_left, value="EDP").pack(anchor=tk.W)

        # Créer un Frame pour les boutons radio à droite (Linéaire/Non linéaire)
        butoton_radio_regualar_left_frame = ttk.Frame(top_options_frame)
        butoton_radio_regualar_left_frame.grid(row=0, column=1, sticky=tk.E, padx=10)
        # Ajouter les boutons radio "Linéaire" et "Non Linéaire" à droite
        tk.Radiobutton(butoton_radio_regualar_left_frame, text="Linéaire", variable=self.radio_var_regular_left, value="Linéaire").pack(anchor=tk.W)
        tk.Radiobutton(butoton_radio_regualar_left_frame, text="Non Linéaire", variable=self.radio_var_regular_left, value="Non Linéaire").pack(anchor=tk.W)
        
        # Exemple de champs de saisie numérique des pas
        label_temps = tk.Label(top_options_frame, text="Intervalle de temps (debut, fin) :", font=("Arial", 10))
        label_temps.grid(row=3, column=0, sticky=tk.E, padx=10)
        # Ajouter une validation stricte en empêchant tout caractère non numérique ou non "-" et "."
        vcmd = (self.root.register(self.validate_real_number_input), '%P')
        self.entry_param1 = tk.Entry(top_options_frame, validate="key", validatecommand=vcmd)
        self.entry_param1.grid(row=3, column=1, sticky=tk.E, padx=5)
        validate_btn1 = tk.Button(top_options_frame, text="Valider", command=self.on_validate_param1)
        validate_btn1.grid(row=3, column=2, sticky=tk.E, padx=5)

        label_pas_temporel = tk.Label(top_options_frame, text="Pas Temporel :", font=("Arial", 10))
        label_pas_temporel.grid(row=4, column=0, sticky=tk.E, padx=10)
        # Ajouter une validation stricte en empêchant tout caractère non numérique ou non "-" et "."
        vcmd = (self.root.register(self.validate_real_number_input), '%P')
        self.entry_param2 = tk.Entry(top_options_frame, validate="key", validatecommand=vcmd)
        self.entry_param2.grid(row=4, column=1, sticky=tk.E, padx=5)
        validate_btn2 = tk.Button(top_options_frame, text="Valider", command=self.on_validate_param1)
        validate_btn2.grid(row=4, column=2, sticky=tk.E, padx=5)


        label_espace = tk.Label(top_options_frame, text="Intervalle d'espace (début, fin) :", font=("Arial", 10))
        label_espace.grid(row=5, column=0,  sticky=tk.E, padx=10)
        vcmd = (self.root.register(self.validate_real_number_input), '%P')
        self.entry_param3 = tk.Entry(top_options_frame, validate="key", validatecommand=vcmd)
        self.entry_param3.grid(row=5, column=1, sticky=tk.E, padx=5)
        validate_btn3 = tk.Button(top_options_frame, text="Valider", command=self.on_validate_param2)
        validate_btn3.grid(row=5, column=2, sticky=tk.E, padx=5)

        label_pas_espace = tk.Label(top_options_frame, text="Pas Spatial :", font=("Arial", 10))
        label_pas_espace.grid(row=6, column=0,  sticky=tk.E, padx=10)
        vcmd = (self.root.register(self.validate_real_number_input), '%P')
        self.entry_param4 = tk.Entry(top_options_frame, validate="key", validatecommand=vcmd)
        self.entry_param4.grid(row=6, column=1, sticky=tk.E, padx=5)
        validate_btn4 = tk.Button(top_options_frame, text="Valider", command=self.on_validate_param2)
        validate_btn4.grid(row=6, column=2, sticky=tk.E, padx=5)

        


    def black_scholes_call(self, S, K, T, r, sigma):
        """Calcule le prix d'une option d'achat avec le modèle Black-Scholes."""
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
        return call_price

    def show_default_visualization(self):
        """Visualisation de la surface des solutions d'actifs financiers par défaut."""
        self.clear_visualization()  # Clear previous visualization
        
        # Paramètres
        K = 100  # Prix d'exercice
        T = 1    # Temps jusqu'à l'expiration (en années)
        r = 0.05 # Taux d'intérêt (5%)
        sigma = np.linspace(0.1, 0.5, 100)  # Volatilité
        S = np.linspace(50, 150, 100)        # Prix de l'actif sous-jacent

        # Créer une grille de prix de l'actif sous-jacent et de volatilité
        S_grid, sigma_grid = np.meshgrid(S, sigma)
        call_prices = self.black_scholes_call(S_grid, K, T, r, sigma_grid)

        # Créer un graphique en 3D
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        # Tracer la surface
        ax.plot_surface(S_grid, sigma_grid, call_prices, cmap='viridis')

        # Ajouter des labels
        equation = r"$C(S, t) = S N(d_1) - K e^{-rt} N(d_2)$"  # Équation de Black-Scholes
        ax.set_title(f"Prix d'une Option d'Achat (Black-Scholes)\n{equation}", fontsize=12)
        ax.set_xlabel("Prix de l'Actif Sous-Jacent (S)")
        ax.set_ylabel("Volatilité (σ)")
        ax.set_zlabel("Prix de l'Option (Call Price)")

        # Créer un canvas pour afficher le graphique dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.visualization_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear_visualization(self):
        """Effacer la visualisation précédente."""
        for widget in self.visualization_frame.winfo_children():
            widget.destroy()

    def open_equation_window(self):
        """Ouvrir la fenêtre des équations."""
        EquationWindow(self.left_frame)  # Ouvre l'onglet des équations dans la partie gauche

    def open_parameters_window(self):
        """Ouvrir la fenêtre des paramètres."""
        equation_window = EquationFrame(self.root)
        ParametersWindow(self.left_frame)  # Ouvre l'onglet des paramètres dans la partie gauche

    def export_report(self, lang):
        """Exporter le rapport en fonction de la langue sélectionnée."""
        if lang == "fr":
            # Logic to export the report in French
            print("Exporter le rapport en français.")
        else:
            # Logic to export the report in English
            print("Exporting the report in English.")

        ExportWindow(self.left_frame)  # Ouvre l'onglet d'exportation dans la partie gauche

if __name__ == "__main__":
    root = tk.Tk()
    app = EquationSolverApp(root)
    root.mainloop()
