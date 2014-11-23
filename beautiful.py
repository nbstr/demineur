#=========================================#
# BEAUTIFUL                               #
#=========================================#

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

#=========================================#
# INPUT INT                               #
#=========================================#
def input_int(txt="Veuillez entrer un nombre : ", error="!! Vous n'avez pas entré un nombre"):
    """
    Retourne un int envoyé par l'utilisateur avec la gestion des exceptions
    """
    while True:
        try:
            n = int(input(txt))
            break
        except ValueError:
            print (error + "\n")
    return n