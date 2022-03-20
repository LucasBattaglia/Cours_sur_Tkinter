import tkinter as tk
from ligne import *
from rectangle import *
from oval import *
from text import *
from arc import *
from polygone import *

def fen(fenetre):
    fenetre.destroy()
    fenetre2 = tk.Tk()
    fenetre2.title("Canvas")
    fenetre2.attributes("-fullscreen", True)
    fenetre2.config(bg="#87CEEB")

    hauteur, largeur = fenetre2.winfo_screenheight(), fenetre2.winfo_screenwidth()

    # Creation du canvas
    Canevas = tk.Canvas(fenetre2, bg="#87CEEB", height=hauteur-100, width=largeur-100, highlightthickness=3)
    Canevas.pack()

    # Creation du menu
    menu_bar = tk.Menu(fenetre2)

    Dessin_menu = tk.Menu(menu_bar)
    Dessin_menu.add_command(label="une ligne", command=lambda:ligne(Canevas))
    Dessin_menu.add_command(label="un rectangle", command=lambda:rectangle(Canevas))
    Dessin_menu.add_command(label="un oval", command=lambda:oval(Canevas))
    Dessin_menu.add_command(label="du text", command=lambda:text(Canevas))
    Dessin_menu.add_command(label="un polygone", command=lambda:polygone(Canevas))
    Dessin_menu.add_command(label="un arc", command=lambda:arc(Canevas))

    menu_bar.add_cascade(label="Dessiner", menu=Dessin_menu)
    menu_bar.add_command(label="Quitter", command=fenetre2.destroy)

    fenetre2.config(menu=menu_bar)
    fenetre2.mainloop()
