import tkinter

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

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("200x200")

	# Creation du menu
	menu_bar = tkinter.Menu(fenetre)

	Conf_menu = tkinter.Menu(menu_bar, tearoff=0)
	Conf_menu.add_command(label="Joueur", command=Conf_joueur)
	Conf_menu.add_separator()
	Conf_menu.add_command(label="Interface", command=Conf_interface)
	
	profil_menu = tkinter.Menu(menu_bar)
	profil_menu.add_command(label="Ouvrir une autre fenetre", command=fenetre2)
	profil_menu.add_command(label="fermer cette fenetre", command=close)

	menu_bar.add_cascade(label="Configuration", menu=Conf_menu)
	menu_bar.add_cascade(label="Profil", menu=profil_menu)
	menu_bar.add_command(label="Quitter", command=fenetre.destroy)

	fenetre.config(menu=menu_bar)


	fenetre.mainloop()