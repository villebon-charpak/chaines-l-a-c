#QUESTION 4, 5 et 6 - NIVEAU 1.

chaine = input("tapez votre texte")
position = int(input("entrez la position désirée"))      #int pour les nombres car pyton comprend pas
caractere = input("tapez caractère de remplacement")

def substituer(chaine,position,caractere): #faire une fonction à qui on attribue une chaine de caractère, la position du caractère que l'on souhaite changer et enfin le caractère de remplacement 
    liste = list(chaine) # on ne peut pas modifier une chaine donc on crée une liste 
    liste[position] = caractere 
    chaine = ''.join(liste) # on remet la liste en chaine 
    return chaine 


chaine_modifiee = substituer(chaine,position,caractere)
print(chaine_modifiee)
    


