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
difficulte = 9

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
    for ligne in g:
        print ("| " + " | ".join(ligne) + " |\n")
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
    OUTPUT: (x, y) | avec x et y de type int
    """
    pass