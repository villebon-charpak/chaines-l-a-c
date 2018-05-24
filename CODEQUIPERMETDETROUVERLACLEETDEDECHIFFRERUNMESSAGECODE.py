# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:31:07 2018

@author: etudiant
"""

chaine_de_caractere= input("Veuillez saisir votre message codé:")
dico= {}
for lettre in chaine_de_caractere:
    if lettre in dico:
        dico[lettre]= dico[lettre]+1
    else:
        dico[lettre]=1
        
indice_max= dico.keys()[0] # je n'arrive pas à comprendre quel est le problème ici et encore moins à le régler (TypeError: 'dict_keys' object does not support indexing)

for lettre in dico:
    if dico[lettre]> dico[indice_max]:
        indice_max= lettre
print("La lettre la plus fréquente est"+ indice_max)

# Une fois que l'on a le caractère qui se répète le plus souvent, on sait qu'il s'agit en réalité d'un espace.
# Or on peut retrouver le numéro correspondant au caractère en utilisant la fonction nombre= ord(caractère) dans la table ASCII et on sait que l'espace est numéroté à 32
# Donc la clé correspond à la soustraction entre le nombre dans ASCII du caractère représentant l'espace dans le message codé et le nombre représentant réellement l'espace
# Donc clé= nombre-32

nombre= ord(indice_max)
cle= nombre-32

def decaler(caractere, decalage):        # pour éviter d'avoir à redéclarer la fonction, on aurait pu donner le nom de l'exercice dans lequel c'est défini (pas possible ici car le nom du fichier a un espace)
    numero = ord(caractere) + decalage
    return chr(numero)

def déchiffrement_cesar(chaine_de_caractere, cle):
    chiff = ""      #on a nommé cette variable pour pouvoir l'utiliser ensuite et elle est vide parce qu'elle va se remplir au fur et à mesure que la chaine de caractères sera chiffrée
    for char in chaine_de_caractere:  #char permet de s'intéresser à chaque caractère
        chiff = chiff+decaler(char,-1*cle)
    print(chiff)
    return chiff


déchiffrement_cesar(chaine_de_caractere, cle)