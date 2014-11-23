#=========================================#
# HEADER                                  #
#=========================================#

def header(text="DÉMINEUR", vp=1, p=6, m=7, s="#", s2="="):
    """
    Affiche un beau titre.
    """
    padding = p*" "
    margin = m*" "

    void = margin + s + " "*(len(text) + 2*p) + s

    print("\n" + margin + s + s2*(len(text) + 2*p) + s)

    for i in range(vp):
        print(void)

    print(margin + s + padding + text + padding + s)

    for i in range(vp):
        print(void)

    print(margin + s + s2*(len(text) + 2*p) + s + "\n")

header()
    
#=========================================#
# GRILLE                                  #
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

def init_champ():
    """
    Initialise le champ de mines.
    """
    champ = []
    for i in range(9):
        champ.append(["*"] * 9)

    # for bombe in grille:
    #     print ("x: {}, y: {}, valeur: {}".format(bombe[0], bombe[1], grille[bombe]))
    #     plateau[bombe[1]][bombe[0]] = grille[bombe]

    return champ

def print_champ(g):
    """
    Affiche le champ de mines.
    """
    for ligne in g:
        print ("| " + " | ".join(ligne) + " |\n")
    print ("\n")

def bombe(coordonnees):
    """
    Vérifie s'il y a une bombe aux coordonnées indiquées.
    """
    return bombe == coordonnees;

# INITIALISER CHAMP DE MINES
champ = init_champ()
# AFFICHER CHAMP DE MINES
print_champ(champ)



















