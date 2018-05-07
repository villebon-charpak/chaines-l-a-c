#QUESTION 3 - NIVEAU 2

def compter_mot(caractere, pouvoir):
    compteur = 0
    for word in range(len(pouvoir)):
        if pouvoir[word] == caractere:
            compteur += 1
    print(compteur)
    return compteur


compter_mot("lol", pouvoir)
