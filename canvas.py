import tkinter

if __name__ == '__main__':
    # Creation de la fenetre principale
    fenetre = tkinter.Tk()
    fenetre.geometry("240x300")

    # Creation d'un canvas pour mettre des boutons par exemple
    Canvas_fenetre = tkinter.Canvas(fenetre, bg="green", height=50, width=200, highlightthickness=3)
    Canvas_fenetre.pack()
    Bouton_canvas = tkinter.Button(Canvas_fenetre, text="Bouton Canvas", bg="green")
    Bouton_canvas.place(x=50, y=20)

    # Creation d'un canvas pour dessiner par exemple
    Canvas_dessin = tkinter.Canvas(fenetre, bg="green", height=200, width=200, highlightthickness=3)
    Canvas_dessin.pack()

    # Dessiner un trait
    Canvas_dessin.create_line((10, 10), (50, 10))
    Canvas_dessin.create_line((10, 20), (50, 20), width=5, arrow="last", fill="orange")
    Canvas_dessin.create_line((10, 30), (50, 30), (10, 50), (50, 50))

    # Dessinner un rectangle
    Canvas_dessin.create_rectangle((60, 10), (120, 30))
    Canvas_dessin.create_rectangle((130, 10), (170, 50), outline="", fill="orange")

    # Dessiner un oval
    Canvas_dessin.create_rectangle((10, 60), (30, 90), outline="grey")
    Canvas_dessin.create_oval((10, 60), (30, 90))
    Canvas_dessin.create_oval((40, 60), (70, 90))

    # Dessiner du texte
    Canvas_dessin.create_text((90, 90), text="Coucou", anchor=tkinter.SW, font="Arial 15 bold")

    # Dessiner un polygone
    Canvas_dessin.create_polygon((10, 100), (50, 100), (50, 120))
    Canvas_dessin.create_polygon((60, 100), (80, 120), (100, 100), (60, 120))

    # Dessiner un arc
    Canvas_dessin.create_arc((10, 130), (50, 170), extent=100, start=-120)
    Canvas_dessin.create_arc((60, 130), (100, 170), extent=210, start=-120, style=tkinter.ARC)
    Canvas_dessin.create_arc((110, 130), (150, 170), extent=210, start=-10, style=tkinter.CHORD)

    fenetre.mainloop()
