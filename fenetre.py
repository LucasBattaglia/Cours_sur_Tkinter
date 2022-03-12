import tkinter


if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.title("Mon titre")
	fenetre.geometry("700x500")
	fenetre.config(bg="#87CEEB")
	fenetre.iconphoto(True, tkinter.PhotoImage(file="carte-3-T.gif"))

	fenetre.mainloop()