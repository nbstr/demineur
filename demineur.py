#=========================================#
# IMPORTS                                 #
#=========================================#

from beautiful import *
from functions import *

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

# INITIALISER CHAMP DE MINES
champ = init_champ()
# AFFICHER CHAMP DE MINES
print_champ(champ)



















