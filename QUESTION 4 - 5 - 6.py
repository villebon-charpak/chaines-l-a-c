#QUESTION 4, 5 et 6 - NIVEAU 1.

chaine = input("tapez votre texte")
position = int(input("entrez la position d�sir�e")) #int pour les nombre car pyton comprend pas
caractere = input("tapez caract�re de remplacement")

def substituer(chaine,position,caractere): faire une fonction � qui on attribue une chaine de caract�re, la position du caract�re que l'on souhaite changer et enfin le caract�re de remplacement 
    liste = list(chaine) # on ne peux pas modifier une chaine donc on cr�e une liste 
    liste[position] = caractere 
    chaine = ''.join(liste) # on remet la liste en chaine 
    return chaine 


chaine_modifiee = substituer(chaine,position,caractere)
print(chaine_modifiee)
    


