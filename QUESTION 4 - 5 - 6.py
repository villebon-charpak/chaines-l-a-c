#QUESTION 4, 5 et 6 - NIVEAU 1

chaine = input("tapez votre texte")
position = int(input("entrez la position d�sir�e")) #int pour les nombre car pyton comprend pas
caractere = input("tapez caract�re de remplacement")

def substituer(chaine,position,caractere):
    liste = list(chaine)
    liste[position] = caractere 
    chaine = ''.join(liste)
    return chaine 


chaine_modifiee = substituer(chaine,position,caractere)
print(chaine_modifiee)
    


