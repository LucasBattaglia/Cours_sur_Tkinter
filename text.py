import tkinter as tk

def text(canvas):
    def affiche(x, y, text):
        fenetre_conf.destroy()
        canvas.create_text((x, y), text=text)

    fenetre_conf = tk.Toplevel()
    fenetre_conf.title("Cree un Texte")
    fenetre_conf.config(bg="#87CEEB")

    x = tk.StringVar()
    y = tk.StringVar()
    texte = tk.StringVar()

    Texte_x1 = tk.Label(fenetre_conf, text="x de depart: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x1.grid(column=0, row=1)
    Texte_x2 = tk.Label(fenetre_conf, text="x d'arriver: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_x2.grid(column=0, row=2)
    Texte_text = tk.Label(fenetre_conf, text="Texte: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
    Texte_text.grid(column=0, row=3)


    Saisie_x = tk.Entry(fenetre_conf, textvariable=x, bg='bisque', fg='maroon')
    Saisie_x.grid(column=1, row=1)
    Saisie_y = tk.Entry(fenetre_conf, textvariable=y, bg='bisque', fg='maroon')
    Saisie_y.grid(column=1, row=2)
    Saisie_x = tk.Entry(fenetre_conf, textvariable=texte, bg='bisque', fg='maroon')
    Saisie_x.grid(column=1, row=3)

    Bouton = tk.Button(fenetre_conf, text='Confirmer', command=lambda: affiche(x.get(), y.get(), texte.get()))
    Bouton.grid(column=2, row=5)
