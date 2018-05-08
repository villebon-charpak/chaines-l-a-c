#QUESTIONS 1 ET 2 - NIVEAU 1

#QUESTION 1

chaine = input("Veuillez saisir du texte")


def compter_occurences(caractere, chaine):
    compteur = 0
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            compteur += 1
    print(compteur)
    return compteur

compter_occurences("u", chaine)

#QUESTION 2

chaine = input("Veuillez saisir du texte")

def compter_mots(chaine):
    if chaine == '': # si la chaine est vide, il y a 0 mot
        return 0
    else :
       compteur = compter_occurences(' ', chaine)
       compteur = 1 + compteur
       print(compteur)
       return compteur


compter_occurences(" ", chaine)
