#=========================================#
# IMPORTS                                 #
#=========================================#
from beautiful import *
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
    # AFFICHER CHAMP DE MINES
    print_champ(champ)

main()



















