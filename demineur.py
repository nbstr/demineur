#=========================================#
# IMPORTS                                 #
#=========================================#
from functions import *

#=========================================#
# MAIN                                    #
#=========================================#
def main():
    """
    Application principale
    """
    # TITRE BEAUTIFUL
    header()
    # INITIALISER CHAMP DE MINES
    champ = init_champ()
    
    # DEMANDER COORDONNÉES
    while True:
    	# AFFICHER CHAMP DE MINES
        print_champ(champ)
        coordonnees = input_coordonnees()
        print (coordonnees)
        if(bombe(coordonnees)):
            print ("\n\n!!! BOOM !!!\n\n")
            break
        else:
            print ("\n\n..ouf\n\n")
    
    # GAME OVER
    header("GAME OVER")


main()



















