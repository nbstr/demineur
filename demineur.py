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
    	input_coordonnees()

main()



















