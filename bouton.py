import tkinter


def affiche_hello():
	print("hello")


if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("200x200")

	# Creation d'un bouton poussoir
	Bouton = tkinter.Button(fenetre, text="Bienvenue", bg="green", activebackground="Yellow", activeforeground="blue", command=affiche_hello)
	Bouton.pack()

	Bouton_desactiver = tkinter.Button(fenetre, text="Bienvenue", bg="Yellow", activebackground="Yellow", activeforeground="blue", state=tkinter.DISABLED, command=affiche_hello)
	Bouton_desactiver.pack()

	fenetre.mainloop()
