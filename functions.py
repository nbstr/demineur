#=========================================#
# IMPORTS                                 #
#=========================================#
from beautiful import *
from random import randint

#=========================================#
# CONFIG                                  #
#=========================================#  

# DIFFICULTÉ
nb_cases = 9 # !! MAX 26
nb_bombes = 9 # !! MAX nb_cases**2

# SECURITÉ
if(nb_bombes >= nb_cases**2):
    nb_bombes = nb_cases**2 - 1

# COORDONNÉES
alpha_maj = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alpha_num = list(range(1, nb_cases + 1))

#=========================================#
# FUNCTIONS                               #
#=========================================#
def generer_bombes(hasard=False):
    """
    Génère et place des bombes au hasard.
    """
    if(hasard):
        grille = {}
        while len(grille) < (nb_bombes):
            x = randint(0, nb_cases-1)
            y = randint(0, nb_cases-1)
            grille[(x, y)] = "B"
        return grille
    else:
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
        return grille

def init_champ():
    """
    Initialise le champ de mines.
    """
    champ = []
    for i in range(nb_cases):
        champ.append(["*"] * nb_cases)
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

def bombe(coord, grille):
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
    # VALIDATION Y
    while True:
        y = input("• Veuillez entrer la lettre d’une ligne: ")
        try:
            y = int(alpha_maj[:nb_cases].index(y.upper()))
            break
        except ValueError:
            print("!! La lettre de la ligne est invalide\n")

    # VALIDATION X
    while True:
        x = input_int("• Veuillez entrer le numéro d’une colonne: ")
        if(x < 1 or x > nb_cases):
            print ("!! Le numéro de la colonne est invalide\n")
        else:
            x -= 1
            break

    return (x, y)

def compte_bombes(x, y, grille):
    """
    Compte le nombre de bombes aux alentours.
    """ 
    nombre_bombes = 0

    for ligne in range(y-1, y+2):
        for colonne in range(x-1, x+2):
            # VERIFIER SI ON EST TOUJOURS SUR LE CHAMP DE MINES
            if(colonne >= 0 and colonne < nb_cases and ligne >= 0 and ligne < nb_cases and (ligne != y or colonne != x)):
                if(bombe((colonne, ligne), grille)):
                    nombre_bombes += 1
    else:
        return nombre_bombes

def afficher_case(champ, x, y, grille):
    """
    Affiche le nombre de bombes adjacentes.
    """ 
    nombre_bombes = compte_bombes(x, y, grille)

    # REMPLIR LA CASE
    if(nombre_bombes == 0):
        champ[y][x] = " "
        # AFFICHER LES CASES ADJACENTES
        for l in range(y-1, y+2):
            for c in range(x-1, x+2):
                # VERIFIER SI ON EST TOUJOURS SUR LE CHAMP DE MINES
                if(c >= 0 and c < nb_cases and l >= 0 and l < nb_cases and (l != y or c != x) and champ[l][c] == "*"):
                    sous_compte = compte_bombes(c, l, grille)
                    if(sous_compte == 0):
                        champ[l][c] = " "
                        champ = afficher_case(champ, c, l, grille)
                    else:
                        champ[l][c] = str(compte_bombes(c, l, grille))
        
    else:
        champ[y][x] = str(nombre_bombes)

    return champ

def fin(champ, grille):
    count = 0
    for ligne in champ:
        for element in ligne:
            if(element == "*"):
                count += 1
    return count == len(grille)
















