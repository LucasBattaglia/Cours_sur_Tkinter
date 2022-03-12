import tkinter

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("200x200")
	
	# Creation de texte
	Texte = tkinter.Label(master=fenetre, text="Bienvenue", bg="green", font=("Ink Free", 20), justify= tkinter.CENTER, underline=0, relief=tkinter.GROOVE)
	Texte.pack()

	fenetre.mainloop()
