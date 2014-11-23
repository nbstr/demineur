#=========================================#
# IMPORTS                                 #
#=========================================#
from beautiful import *

#=========================================#
# CONFIG                                  #
#=========================================#  

# BOMBES
grille = {}
grille [(0 ,7)] = "B"
grille [(1 ,5)] = "B"
grille [(1 ,6)] = "B"
grille [(1 ,8)] = "B"
grille [(2 ,4)] = "B"
grille [(3 ,4)] = "B"
grille [(5 ,5)] = "B"
grille [(5 ,7)] = "B"
grille [(7 ,0)] = "B"
grille [(7 ,5)] = "B"

# DIFFICULTÉ
difficulte = 9 # !! MAX 26

# COORDONNÉES
alpha_maj = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alpha_num = list(range(1, difficulte + 1))

#=========================================#
# FUNCTIONS                               #
#=========================================#

def init_champ():
    """
    Initialise le champ de mines.
    """
    champ = []
    for i in range(difficulte):
        champ.append(["*"] * difficulte)
    return champ

def print_champ(g):
    """
    Affiche le champ de mines.
    """
    print ("\n\n    " + "   ".join(str(col) for col in alpha_num))

    print ("  " + "-"*37)
    for i, ligne in enumerate(g):
        print (alpha_maj[i] + " | " + " | ".join(ligne) + " |\n  " + "-"*37)
    print ("\n")

def bombe(coord):
    """
    Vérifie s'il y a une bombe aux coordonnées indiquées.
    """
    for bombe in grille:
        if (bombe == coord):
            return True;
    return False;

def input_coordonnees():
    """
    Demande au joueur de selectionner une case.
    """    
    # VALIDATION X
    while True:
        x = input_int("• Veuillez entrer le numéro d’une colonne: ")
        if(x < 1 or x > difficulte):
            print ("!! Le numéro de la colonne est invalide\n")
        else:
            x -= 1
            break

    # VALIDATION Y
    while True:
        y = input("• Veuillez entrer la lettre d’une ligne: ")
        try:
            y = int(alpha_maj[:difficulte].index(y.upper()))
            break
        except ValueError:
            print("!! La lettre de la ligne est invalide\n")

    return (x, y)

def compte_bombes(x, y):
	"""
	Compte le nombre de bombes aux alentours.
	""" 
	nombre_bombes = 0

	for ligne in range(y-1, y+2):
		for colonne in range(x-1, x+2):
			# VERIFIER SI ON EST TOUJOURS SUR LE CHAMP DE MINES
			if(colonne >= 0 and colonne < difficulte and ligne >= 0 and ligne < difficulte and (ligne != y or colonne != x)):
				if(bombe((colonne, ligne))):
					nombre_bombes += 1
	else:
		return nombre_bombes

def afficher_case(champ, x, y):
	"""
	Affiche le nombre de bombes adjacentes.
	""" 
	nombre_bombes = compte_bombes(x, y)

	# REMPLIR LA CASE
	if(nombre_bombes == 0):
		champ[y][x] = " "
		# AFFICHER LES CASES ADJACENTES
		for l in range(y-1, y+2):
			for c in range(x-1, x+2):
				# VERIFIER SI ON EST TOUJOURS SUR LE CHAMP DE MINES
				if(c >= 0 and c < difficulte and l >= 0 and l < difficulte and (l != y or c != x)):
					sous_compte = compte_bombes(c, l)
					if(sous_compte == 0):
						champ[l][c] = " "
					else:
						champ[l][c] = str(compte_bombes(c, l))
	else:
		champ[y][x] = str(nombre_bombes)

	return champ
















