import tkinter
from tkinter import messagebox

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tkinter.Tk()
	fenetre.geometry("200x200")

	messagebox.showinfo('information', 'Hi! You got a prompt.')
	messagebox.showwarning('warning', 'accept T&C')
	messagebox.showerror('error', 'Something went wrong!')
	messagebox.askquestion('Ask Question', 'Do you want to continue?')
	messagebox.askokcancel('Ok Cancel', 'Are You sure?')
	messagebox.askyesno('Yes|No', 'Do you want to proceed?')
