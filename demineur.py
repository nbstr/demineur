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

        # INPUT
        coordonnees = input_coordonnees()
        
        # BOMBE
        if(bombe(coordonnees)):
            print ("\n\n!!! BOOM !!!\n\n")
            # CONTNUER ?
            CONTINUE = input("\nVoulez vous rejouer ? (oui/non)")
            if(CONTINUE[0].upper() == "O"):
                continue
            else:
                break
        else:
            print ("\n\n..ouf\n\n")
    
    # GAME OVER
    header("GAME OVER")


main()



















