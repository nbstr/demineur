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
    print ("    " + "   ".join(str(col) for col in alpha_num))

    print ("  " + "-"*37)
    for i, ligne in enumerate(g):
        print (alpha_maj[i] + " | " + " | ".join(ligne) + " |\n  " + "-"*37)
    print ("\n")

def bombe(x, y):
    """
    Vérifie s'il y a une bombe aux coordonnées indiquées.
    """
    for bombe in grille:
        if (bombe == (x, y)):
            return True;
    return False;

def input_coordonnees():
    """
    Demande au joueur de selectionner une case.
    INPUT: /
    INPUT USER: "A", "7" (ligne, colonne)
    OUTPUT: (x, y) | avec x et y de type int
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

    print (x, y)