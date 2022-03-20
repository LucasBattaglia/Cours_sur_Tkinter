import tkinter as tk

def rectangle(canvas):
    def affiche(x1, x2,y1,y2):
        fenetre_conf.destroy()
        canvas.create_rectangle((x1, y1), (x2,y2))

    fenetre_conf = tk.Toplevel()
    fenetre_conf.title("Cree une ligne")
    fenetre_conf.config(bg="#87CEEB")

    x1 = tk.StringVar()
    y1 = tk.StringVar()
    x2 = tk.StringVar()
    y2 = tk.StringVar()

    Texte_x1 = tk.Label(fenetre_conf, text="x de depart: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x1.grid(column=0, row=1)
    Texte_x2 = tk.Label(fenetre_conf, text="x d'arriver: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x2.grid(column=0, row=2)
    Texte_y1 = tk.Label(fenetre_conf, text="y de depart: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_y1.grid(column=0, row=3)
    Texte_y2 = tk.Label(fenetre_conf, text="y d'arriver: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_y2.grid(column=0, row=4)

    Saisie_x1 = tk.Entry(fenetre_conf, textvariable=x1, bg='bisque', fg='maroon')
    Saisie_x1.grid(column=1, row=1)
    Saisie_y1 = tk.Entry(fenetre_conf, textvariable=y1, bg='bisque', fg='maroon')
    Saisie_y1.grid(column=1, row=2)
    Saisie_x2 = tk.Entry(fenetre_conf, textvariable=x2, bg='bisque', fg='maroon')
    Saisie_x2.grid(column=1, row=3)
    Saisie_y2 = tk.Entry(fenetre_conf, textvariable=y2, bg='bisque', fg='maroon')
    Saisie_y2.grid(column=1, row=4)

    Bouton = tk.Button(fenetre_conf, text='Confirmer', command=lambda: affiche(x1.get(), x2.get(), y1.get(), y2.get()))
    Bouton.grid(column=2, row=5)
