import tkinter

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("300x200")

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

	fenetre.mainloop()
