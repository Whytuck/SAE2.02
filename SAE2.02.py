##################################################
####### PROGRAMME PROBLEME DES HUITS REINES ######
##################################################


# SAE2.02
# Joseph ESTERLINGOT
# John DELHOUYA
# Louis MILIN

N = 8


# Fonction pour afficher l'échiquier
def afficher_echiquier(echiquier):
    for ligne in echiquier:
        for case in ligne:
            print("♕" if case == 1 else ".", end=" ")
        print()

# Fonction pour vérifier si une reine peut être placée à une position donnée
def est_en_securite(echiquier, ligne, colonne):

   

    # Vérification de la colonne
    for i in range(N):
        if i != ligne:
            if echiquier[i][colonne] == 1:
           
                return False
        
    # Vérification de la diagonale gauche
    i, j = ligne, colonne
    while i != N and j != N:
        if i != ligne:
            if echiquier[i][j] == 1:
             
                return False
        i += 1
        j += 1
    
    i, j = ligne, colonne
    while i >= 0 and j >= 0:
        if i != ligne:
            if echiquier[i][j] == 1:
          
                return False
        i -= 1
        j -= 1

    # Vérification de la diagonale droite          
    i, j = ligne, colonne
    while i != N and j >= 0:
        if i != ligne:
            if echiquier[i][j] == 1:
          
                return False
        i += 1
        j -= 1

    i, j = ligne, colonne
    while i >= 0 and j != N:
        if i != ligne:
            if echiquier[i][j] == 1:
    
                return False
        i -= 1
        j += 1 

    return True


# Fonction de backtracking
def backtracking(ligne, ligne_deb, echiquier, solutions):

    if ligne == N:
        solutions.append([row[:] for row in echiquier])
        return
    
    if ligne == ligne_deb:
        backtracking(ligne+1, ligne_deb,echiquier, solutions)
    
    else:
        for colonne in range (N):
            if est_en_securite(echiquier, ligne, colonne):

                echiquier[ligne][colonne] = 1
                backtracking(ligne+1, ligne_deb,echiquier, solutions)
                echiquier[ligne][colonne] = 0

    return


def main ():

    # Initialisation de l'echiquier
    echiquier = [[0] * N for i in range(N)]


    # Choix de la position de la première reine par l'utilisateur
    print("Choisissez la position de la première reine en indiquant la ligne et la colonne.")
    ligne = int(input("Ligne : ")) - 1
    colonne = int(input("Colonne : ")) - 1
    echiquier[ligne][colonne] = 1

    solutions = []

    backtracking(0, ligne,echiquier, solutions)

    for sol in solutions:
        print("---------------")
        afficher_echiquier(sol)


# Appel de la fonction principale
if __name__ == "__main__":
    main()