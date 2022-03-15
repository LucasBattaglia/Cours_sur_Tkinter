import tkinter
from tkinter import messagebox


def affiche_hello():
    print("hello")


def Conf_joueur():
    print("Configuration du joueur")


def Conf_interface():
    print("Configuration de l'interface")


def fenetre2():
    global fenetre2
    fenetre2 = tkinter.Toplevel(fenetre)


def close():
    global fenetre2
    fenetre2.destroy()


def showinfo():
    messagebox.showinfo("Info", "Welcome to WayToLearnX!")


def showwarning():
    messagebox.showwarning('warning', 'accept T&C')


def showerror():
    messagebox.showerror('error', 'Something went wrong!')


def askquestion():
    messagebox.askquestion('Ask Question', 'Do you want to continue?')


def askokcancel():
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')


def askyesno():
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')


if __name__ == '__main__':
    # Creation de la fenetre principale
    fenetre = tkinter.Tk()
    fenetre.title("Mon titre")
    fenetre.geometry("700x500")
    fenetre.config(bg="#87CEEB")
    fenetre.iconphoto(True, tkinter.PhotoImage(file="carte-3-T.gif"))
    fenetre.minsize(50, 50)

    # Creation de texte
    Texte = tkinter.Label(master=fenetre, text="Bienvenue", bg="green", font=("Ink Free", 20), justify=tkinter.CENTER,
                          underline=0, relief=tkinter.GROOVE)
    Texte.grid(column=0, row=0)

    # Creation d'un bouton poussoir
    Bouton = tkinter.Button(fenetre, text="Bouton Normal", bg="green", activebackground="Yellow",
                            activeforeground="blue", command=affiche_hello)
    Bouton.grid(column=0, row=1)

    Bouton_desactiver = tkinter.Button(fenetre, text="Bouton Desactiver", bg="Yellow", activebackground="Yellow",
                                       activeforeground="blue", state=tkinter.DISABLED, command=affiche_hello)
    Bouton_desactiver.grid(column=1, row=1)

    # Creation d'un canvas pour mettre des boutons par exemple
    Canvas_fenetre = tkinter.Canvas(fenetre, bg="green", height=50, width=200, highlightthickness=3)
    Canvas_fenetre.grid(column=0, row=2)
    Bouton_canvas = tkinter.Button(Canvas_fenetre, text="Bouton Canvas", bg="green")
    Bouton_canvas.place(x=50, y=20)

    # Creation d'un canvas pour dessiner par exemple
    Canvas_dessin = tkinter.Canvas(fenetre, bg="green", height=200, width=200, highlightthickness=3)
    Canvas_dessin.grid(column=1, row=2)

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

    # Creation de case a cocher
    Var = tkinter.StringVar()
    print(Var.get())
    BR1 = tkinter.Radiobutton(fenetre, text="Par défaut", variable=Var, value="blue", bg=None)
    BR1.grid(column=0, row=3)
    BR2 = tkinter.Radiobutton(fenetre, text="Blanc", variable=Var, value="white", bg=None)
    BR2.grid(column=1, row=3)
    BR3 = tkinter.Radiobutton(fenetre, text="Noir", variable=Var, value="black", bg=None)
    BR3.grid(column=2, row=3)

    Var1 = tkinter.StringVar()
    print(Var1.get())
    VarB1 = tkinter.StringVar()
    print(VarB1.get())
    VarB2 = tkinter.StringVar()
    print(VarB2.get())
    BC1 = tkinter.Checkbutton(fenetre, text="Francais", variable=Var1, bg=None)
    BC1.grid(column=0, row=4)
    BC2 = tkinter.Checkbutton(fenetre, text="Anglais", variable=VarB1, bg=None)
    BC2.grid(column=1, row=4)
    BC3 = tkinter.Checkbutton(fenetre, text="Espagnol", variable=VarB2, bg=None)
    BC3.grid(column=2, row=4)

    Var2 = tkinter.StringVar()
    Var2.set("Chocolat")
    print(Var2.get())
    BR4 = tkinter.Radiobutton(fenetre, text="Chocolat", variable=Var2, value="Chocolat", bg=None, indicatoron=0)
    BR4.grid(column=0, row=5)
    BR5 = tkinter.Radiobutton(fenetre, text="Cafe", variable=Var2, value="cafe", bg=None, indicatoron=0)
    BR5.grid(column=1, row=5)
    BR6 = tkinter.Radiobutton(fenetre, text="The", variable=Var2, value="The", bg=None, indicatoron=0)
    BR6.grid(column=2, row=5)

    # Creation d'une saisie utilisateur
    VarS = tkinter.StringVar()
    print(VarS.get())
    Saisie = tkinter.Entry(fenetre, textvariable=VarS, bg='bisque', fg='maroon')
    Saisie.grid(column=0, row=6)
    VarS1 = tkinter.StringVar()
    print(VarS1.get())
    Saisie2 = tkinter.Entry(fenetre, textvariable=VarS1, show="*")
    Saisie2.grid(column=1, row=6)

    # Creation du menu
    menu_bar = tkinter.Menu(fenetre)

    Conf_menu = tkinter.Menu(menu_bar, tearoff=0)
    Conf_menu.add_command(label="Joueur", command=Conf_joueur)
    Conf_menu.add_separator()
    Conf_menu.add_command(label="Interface", command=Conf_interface)

    profil_menu = tkinter.Menu(menu_bar)
    profil_menu.add_command(label="Ouvrir une autre fenetre", command=fenetre2)
    profil_menu.add_command(label="fermer cette fenetre", command=close)

    menu_erreur = tkinter.Menu(menu_bar, tearoff=0)
    menu_erreur.add_command(label="d'information", command=showinfo)
    menu_erreur.add_command(label="d'avertissement", command=showwarning)
    menu_erreur.add_command(label="d'erreur", command=showerror)
    menu_erreur.add_command(label="d'interogation", command=askquestion)
    menu_erreur.add_command(label="de confirmation (OK/Cancel)", command=askokcancel)
    menu_erreur.add_command(label="de confirmation (Yes/No)", command=askyesno)

    menu_bar.add_cascade(label="Configuration", menu=Conf_menu)
    menu_bar.add_cascade(label="fenetre secondaire", menu=profil_menu)
    menu_bar.add_cascade(label="fenetre d'erreur", menu=menu_erreur)
    menu_bar.add_command(label="Quitter", command=fenetre.destroy)

    fenetre.config(menu=menu_bar)

    # Creation de fenetre d'erreur

    fenetre.mainloop()
