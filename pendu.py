# -*-coding: utf-8 -*

import os
import math
import pickle
import fonctions
import données
import random

#création ou récupération du dictionnaire des scores, dans le fichier scores

try :
	with open("scores","rb") as fichier:
		le_depickler=pickle.Unpickler(fichier)
		dico_scores=le_depickler.load()	

except FileNotFoundError :
	dico_scores={}
	with open("scores", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(dico_scores)

print("Bienvenu dans ce jeu du pendu !")

continuer=True

while continuer==True :

	#choix ou changement du pseudo
	pseudo=fonctions.choix_pseudo()
	

	#on met le pseudo en majuscules
	pseudo=pseudo.upper()
	
	
	#on accueille comme il se doit le (nouveau) joueur, en lui donnant ses scores
	fonctions.accueil_joueur(pseudo,dico_scores)

	
	#initialisation des données de jeu pour ce nouveau pseudo
	nb_parties=0
	score=0
	points_gagnes=0
	

	#boucle de jeu avec pseudo inchangé
	
	
	continuer_meme_pseudo=True
	
	while continuer_meme_pseudo==True:
		
		#choix du mot et initialisation des variables de la partie
		print("\nVous allez jouer votre partie numéro",nb_parties+1)
		mot=données.liste_mots[random.randrange(len(données.liste_mots))]
		mot_affiche="********"
	
		coups_restants=8
		lettres_proposees=""
		
		#début du game
		while coups_restants > 0:
			
			#choix d'une lettre
			lettre=fonctions.choix_lettre(lettres_proposees,mot_affiche)
			
			#mise à jour de la liste de lettres proposées
			if lettres_proposees=="":
				lettres_proposees=lettre
			else:
				lettres_proposees=lettres_proposees+", "+lettre
			
			print("-----------")
			#test de la lettre proposée
			if lettre not in mot:
				print("\nAh non, désolé, cette lettre ne figure pas dans le mot !")
				coups_restants -= 1
				fonctions.dessin_pendu(coups_restants)
				if coups_restants==0:
					print("\nLe mot à trouver était... "+mot)
			else :
				print("\nBien joué ! La lettre "+lettre+" est bien dans le mot recherché")
				mot_affiche=fonctions.change_mot_affiche(mot,mot_affiche,lettre)
				if "*" in mot_affiche :
					print("Vous vous rapprochez du but\n")
				else :
					print("\nFELICITATIONS ! Vous avez trouvé le mot "+mot+" avant de succomber, vous marquez",coups_restants,"point(s).")
					points_gagnes=coups_restants
					coups_restants=0
		
		print("\n-----------\n-----------\nPartie numéro",nb_parties+1,"terminée.\n")
		score += points_gagnes	
		nb_parties += 1
		print("votre score sur cette session est de",score,"point(s) en ",nb_parties,"partie(s), soit une moyenne de",round(score/nb_parties,2),"points par partie jouée.")
		fonctions.mettre_a_jour_score(dico_scores,pseudo,points_gagnes)
		
		
		
		arret=input("\nVoulez-vous continuer à jouer ?(o/n)")
		if arret.lower()!="o":
			continuer_meme_pseudo=False
			continuer=False
		else:
			suite=input("Voulez-vous continuer sous le même pseudo ?(o/n)")
			if suite.lower() != "o":
				continuer_meme_pseudo=False


#liste des scores affichée à la fin du jeu
print("\n---------\nrécapitulatif des scores :")
for nom in dico_scores.keys():
	print(nom+" "*(9-len(nom))+":",dico_scores[nom][0],"points en",dico_scores[nom][1],"parties, soit",dico_scores[nom][2],"points par partie")

print("\nA bientôt !")
				
with open("scores","wb") as fichier:
	lepickler=pickle.Pickler(fichier)
	lepickler.dump(dico_scores)
						


	
os.system("pause")
