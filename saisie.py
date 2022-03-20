import tkinter

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("200x200")

	# Creation d'une saisie utilisateur
	VarS = tkinter.StringVar()
	print(VarS.get())
	Saisie = tkinter.Entry(fenetre, textvariable=VarS, bg='bisque', fg='maroon')
	Saisie.pack()
	VarS1 = tkinter.StringVar()
	print(VarS1.get())
	Saisie2 = tkinter.Entry(fenetre, textvariable=VarS, show="*")
	Saisie2.pack()

	fenetre.mainloop()
