from tkinter import messagebox
import tkinter as tk
import fonction_de_l_exercice as fonc
import fenetreexo as f


def verif(adresse, mdp, conf, fenetre):
	if not fonc.Verif_mdp(mdp, conf):
		messagebox.showerror("Erreur de mots de passe", 'Veuillez entrer 2 fois le meme mots de passe')
		MDP.set("")
		CMDP.set("")
	elif not fonc.Verif_adresse(adresse):
		reponce = messagebox.askyesno('Adresse non reconnu', 'Votre adresse ne semble pas correct\nVoulez vous la modifier?')
		if not reponce:
			f.fen(fenetre=fenetre)
	else:
		f.fen(fenetre=fenetre)

if __name__ == '__main__':
	# Creation de la fenetre principale
	fenetre = tk.Tk()
	fenetre.title("Enregistrement")
	fenetre.geometry("700x500")
	fenetre.config(bg="#87CEEB")
	fenetre.iconphoto(True, tk.PhotoImage(file="logo.gif"))

	# Nom
	Texte_nom = tk.Label(master=fenetre, text="Nom: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_nom.grid(column=0, row=0)

	Nom = tk.StringVar()
	SaisieNom = tk.Entry(fenetre, textvariable=Nom, bg='bisque', fg='maroon')
	SaisieNom.grid(column=1, row=0)

	# Prenom
	Texte_prenom = tk.Label(master=fenetre, text="Prenom: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_prenom.grid(column=0, row=1)

	Prenom = tk.StringVar()
	SaisiePrenom = tk.Entry(fenetre, textvariable=Prenom, bg='bisque', fg='maroon')
	SaisiePrenom.grid(column=1, row=1)

	# Pseudo
	Texte_Pseudo = tk.Label(fenetre, text="Pseudo: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_Pseudo.grid(column=0, row=2)
	SaisiePseudo = tk.Label(fenetre, textvariable=Prenom, bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	SaisiePseudo.grid(column=1, row=2)

	# Genre
	Texte_Genre = tk.Label(fenetre, text="Genre: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_Genre.grid(column=4, row=0, padx=30)

	Genre = tk.StringVar()

	Masculin = tk.Radiobutton(fenetre, text="Masculin", variable=Genre, value="Masculin", bg=None)
	Masculin.grid(column=4, row=1, padx=30)

	Feminin = tk.Radiobutton(fenetre, text="Feminin", variable=Genre, value="Feminin", bg=None)
	Feminin.grid(column=4, row=2, padx=30)

	NP = tk.Radiobutton(fenetre, text="Non preciser", variable=Genre, value="Non preciser", bg=None, command=lambda: messagebox.showinfo('Genre', 'Nous ne pourrons pas vous proposer certain article!'))
	NP.grid(column=4, row=3, padx=30)

	# adresse mail
	Texte_Adresse = tk.Label(fenetre, text="Votre adresse mail: ", bg="#87CEEB", font=("Ink Free", 20),
							 justify=tk.CENTER)
	Texte_Adresse.grid(column=0, row=3)

	adresse = tk.StringVar()

	SaisieAdresse = tk.Entry(fenetre, textvariable=adresse, bg='bisque', fg='maroon')
	SaisieAdresse.grid(column=1, row=3)

	# Mots de passe
	Texte_MDP = tk.Label(fenetre, text="Mots De Passe: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_MDP.grid(column=0, row=4)

	MDP = tk.StringVar()

	SaisieMDP = tk.Entry(fenetre, textvariable=MDP, bg='bisque', fg='maroon', show="*")
	SaisieMDP.grid(column=1, row=4)

	# Confirmation du Mots de passe
	Texte_CMDP = tk.Label(fenetre, text="Confimation Du Mots De Passe: ", bg="#87CEEB", font=("Ink Free", 20), justify=tk.CENTER)
	Texte_CMDP.grid(column=0, row=5)

	CMDP = tk.StringVar()

	SaisieCMDP = tk.Entry(fenetre, textvariable=CMDP, bg='bisque', fg='maroon', show='*')
	SaisieCMDP.grid(column=1, row=5)

	# Bouton Confirmer
	Confirme = tk.Button(fenetre, text="Suivant", command=lambda: verif(mdp=MDP.get(), conf=CMDP.get(), adresse=adresse.get(), fenetre=fenetre))
	Confirme.grid(column=3, row=6)






	fenetre.mainloop()

