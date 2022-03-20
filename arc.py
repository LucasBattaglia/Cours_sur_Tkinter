import tkinter as tk

def arc(canvas):
    def affiche(x1, x2, y1, y2, debut, angle, style):
        fenetre_conf.destroy()
        canvas.create_arc((x1, y1), (x2, y2),start=debut, extent=angle, style=style)
    fenetre_conf = tk.Toplevel()
    fenetre_conf.title("Cree un arc")
    fenetre_conf.config(bg="#87CEEB")

    x1 = tk.StringVar()
    y1 = tk.StringVar()
    x2 = tk.StringVar()
    y2 = tk.StringVar()
    style = tk.Variable()
    debut = tk.StringVar()
    angle = tk.StringVar()

    Texte_x1 = tk.Label(fenetre_conf, text="x de depart: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x1.grid(column=0, row=1)
    Texte_x2 = tk.Label(fenetre_conf, text="x d'arriver: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x2.grid(column=0, row=2)
    Texte_y1 = tk.Label(fenetre_conf, text="y de depart: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_y1.grid(column=0, row=3)
    Texte_y2 = tk.Label(fenetre_conf, text="y d'arriver: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_y2.grid(column=0, row=4)
    Texte_debut=tk.Label(fenetre_conf, text="Angle avec le premier \npoint et la droite \npartant vers l'est: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_debut.grid(column=0, row=6)
    Texte_angle = tk.Label(fenetre_conf, text="Angle du tracer: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_angle.grid(column=0, row=7)

    Saisie_x1 = tk.Entry(fenetre_conf, textvariable=x1, bg='bisque', fg='maroon')
    Saisie_x1.grid(column=1, row=1)
    Saisie_y1 = tk.Entry(fenetre_conf, textvariable=y1, bg='bisque', fg='maroon')
    Saisie_y1.grid(column=1, row=2)
    Saisie_x2 = tk.Entry(fenetre_conf, textvariable=x2, bg='bisque', fg='maroon')
    Saisie_x2.grid(column=1, row=3)
    Saisie_y2 = tk.Entry(fenetre_conf, textvariable=y2, bg='bisque', fg='maroon')
    Saisie_y2.grid(column=1, row=4)
    Saisie_debut = tk.Entry(fenetre_conf, textvariable=debut, bg='bisque', fg='maroon')
    Saisie_debut.grid(column=1, row=6)
    Saisie_angle = tk.Entry(fenetre_conf, textvariable=angle, bg='bisque', fg='maroon')
    Saisie_angle.grid(column=1, row=7)

    normal = tk.Radiobutton(fenetre_conf, text="Normal", variable=style, value=None, bg="#87CEEB")
    normal.grid(column=2, row=1, padx=5)
    arc = tk.Radiobutton(fenetre_conf, text="Arc", variable=style, value=tk.ARC, bg="#87CEEB")
    arc.grid(column=3, row=1)
    chord = tk.Radiobutton(fenetre_conf, text="Chord", variable=style, value=tk.CHORD, bg="#87CEEB")
    chord.grid(column=4, row=1)


    Bouton = tk.Button(fenetre_conf, text='Confirmer', command=lambda: affiche(x1.get(), x2.get(), y1.get(), y2.get(), debut.get(), angle.get(), style.get()))
    Bouton.grid(column=2, row=8)