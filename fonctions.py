# -*-coding: utf-8 -*

import os
import math
import random


#fonction enlevant les accents d'une chaîne
def enlever_accents(chaine):
	accent = ['é', 'è', 'ê', 'ë', 'à', 'ä', 'ù', 'û', 'ü', 'ç', 'ô', 'ö', 'î', 'ï', 'â']
	sans_accent = ['e', 'e', 'e', 'e', 'a', 'a', 'u', 'u', 'u', 'c', 'o', 'o', 'i', 'i', 'a']
 
	for i in range(len(accent)):
		chaine = chaine.replace(accent[i], sans_accent[i])
	return chaine


#choix ou changement du pseudo
def choix_pseudo():
	pseudo=""
	while pseudo=="":
		pseudo=input("Entrez votre pseudo (moins de 8 caractères)\n")
		if pseudo=="":
			print("Vous n'avez pas choisi de pseudo !")
		elif len(pseudo)>8:
			print("Vous avez dépassé 8 caractères !")
			pseudo=""
	return pseudo


#fonction changeant la chaîne montrée au joueur lorsque la lettre proposée est bonne
def change_mot_affiche(mot_a_trouver,chaine,lettre):
	for i in range(len(mot_a_trouver)):
		if mot_a_trouver[i]==lettre:
			if i==0:
				chaine=lettre+chaine[i+1:]
			elif i==len(mot_a_trouver)-1:
				chaine=chaine[:i]+lettre
			else:
				chaine=chaine[:i]+lettre+chaine[i+1:]
	return chaine

	
#fonction mettant à jour et affichant le score du participant sur la session
def mettre_a_jour_score_session(score,nb_parties,points_gagnes):

	print("votre score sur cette session est de",score,"point(s) en ",nb_parties,"partie(s), soit une moyenne de",score/nb_parties,"points par partie jouée.")
	

	
#fonction mettant à jour et affichant le score global du participant
def mettre_a_jour_score(dico_scores,pseudo,points_gagnes):
	dico_scores[pseudo][0]+= points_gagnes
	dico_scores[pseudo][1]+= 1
	dico_scores[pseudo][2]= round(dico_scores[pseudo][0]/dico_scores[pseudo][1],2)
	
	print("votre score cumulé total est de :",dico_scores[pseudo][0],"points en",dico_scores[pseudo][1],"parties, soit une moyenne de",dico_scores[pseudo][2],"points par partie jouée.")
	



def accueil_joueur(pseudo,dico_scores):	
	if dico_scores=={}:
		print("\n==================\nWelcome, "+pseudo+" !")
		dico_scores[pseudo]=[0,0,0]
	elif pseudo in dico_scores :
		print("\n==================\nWelcome back, "+pseudo+" !")
		print("votre score cumulé total est de :",dico_scores[pseudo][0],"points en",dico_scores[pseudo][1],"parties, soit une moyenne de",dico_scores[pseudo][2],"points par partie jouée. Voyons ce que cela donnera cette fois-ci !")
	else:
		print("\n==================\nWelcome, "+pseudo+" !")
		dico_scores[pseudo]=[0,0,0]
	


def choix_lettre(lettres_proposees,mot_affiche):
	lettre=""		
	print("\nVoici le mot recherché : "+mot_affiche)
	#choix d'une lettre
	while lettre=="":
		if lettres_proposees=="":
			lettre = input("Toutes les lettres sont encore disponibles. Quelle lettre proposez-vous ?\n")
		else :
			print("Lettre(s) déjà proposée(s) : "+lettres_proposees)
			lettre = input("\nQuelle lettre proposez-vous ?\n")

		lettre = lettre.upper()
				
		if lettre=="":
			print("\nIl faut entrer quelque chose ! Une lettre, de préférence.\n")
		elif len(lettre)>1:
			print("\nVous avez saisi plus d'un caractère !\n")
			lettre=""
		elif lettre not in "AZERTYUIOPQSDFGHJKLMWXCVBN":
			print("\nVous n'avez pas saisi de lettre !\n")
			lettre=""
		elif lettre in lettres_proposees:
			print("\nAlala, vous avez déjà proposé cela, voyons !\n")
			lettre=""
	return lettre




#fonction affichant le dessin du pendu au fur et à mesure des tentatives
def dessin_pendu(nb):

	if nb==7:
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Un étrange poteau se dresse sur la place du village. Votre piètre première tentative n'y est peut-être pas étrangère...\n")
	
	elif nb==6:
		print("\n     __________")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Les habitants du village, voyant votre détresse, semblent mettre du coeur à l'ouvrage...\n")

	elif nb==5:
		print("\n     __________")
		print("     | //")
		print("     |//")
		print("     |/")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Après vous avoir observé, les villageois décident d'ajouter un renfort structurel à leur ouvrage.\n")

	elif nb==4:
		print("\n     __________")
		print("     | //      |")
		print("     |//       |")
		print("     |/")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   La corde est finalement prête. Vous commencez à trembler.\n")
		
	elif nb==3:
		print("\n     __________")
		print("     | //      |")
		print("     |//       |")
		print("     |/       (_)")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Vous êtes trainé vers la potence. La foule est en délire et vous pleurez.\n")
		
	elif nb==2:
		print("\n     __________")
		print("     | //      |")
		print("     |//       |")
		print("     |/       (_)")
		print("     |         |")
		print("     |         |")
		print("     |         |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Le bourreau vous passe la corde au cou, et les applaudissements redoublent. Vous pensez à toutes ce potentielles tartines de nutella que vous ne pourrez plus jamais manger\n")
		
	elif nb==1:
		print("\n     __________")
		print("     | //      |")
		print("     |//       |")
		print("     |/       (_)")
		print("     |         |")
		print("     |        /|\\")
		print("     |         |")
		print("     |")
		print("     |")
		print("     |")
		print("#####################   Le tabouret est retiré, et vous pendouillez à présent de façon disgracieuse, cherchant désespérement à vous raccrocher à quelque chose afin de ne pas sombrer. Il ne vous reste que quelques instants...\n")

	elif nb==0:
		print("\n     __________")
		print("     | //      |")
		print("     |//       |")
		print("     |/       (_)")
		print("     |         |")
		print("     |        /|\\            PERDU !")
		print("     |         |")
		print("     |        / \\")
		print("     |")
		print("     |")
		print("#####################       Aaaaaarg... Dans un râle insupportable, le vie vous quitte enfin. C'est con, il manquait pas grand chose niveau lettres !\n")


"""		
os.system("pause")
"""
