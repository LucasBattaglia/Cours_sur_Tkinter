import tkinter as tk

def polygone(canvas):
    def affiche(x1, x2, y1, y2, debut, angle):
        fenetre_conf.destroy()
        canvas.create_arc((x1, y1), (x2, y2), start=debut, extent=angle)
    fenetre_conf = tk.Toplevel()
    fenetre_conf.title("Cree un polygone")
    fenetre_conf.config(bg="#87CEEB")

    texte = tk.Label(fenetre_conf, text= "PAS ENCORE DEFINIS")