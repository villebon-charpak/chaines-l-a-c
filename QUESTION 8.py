# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:34:35 2018

@author: etudiant
"""
def decaler(caractere, decalage):        # pour éviter d'avoir à redéclarer la fonction, on aurait pu donner le nom de l'exercice dans lequel c'est défini (pas possible ici car le nom du fichier a un espace)
    nombre = ord(caractere) + decalage
    return chr(nombre)

def chiffrement_cesar(chaine_de_caractere, cle):
    chiff = ""      #on a nommé cette variable pour pouvoir l'utiliser ensuite et elle vide parce qu'elle va se remplir au fur et à mesure que la chaine de caractères sera chiffrée
    for char in chaine_de_caractere:  #char permet de s'intéresser à chaque caractère
        chiff = chiff+decaler(char,cle)
    print(chiff)
    return chiff

chaine_de_caractere = input("Veuillez saisir votre texte:")
cle = int(input("Veuillez saisir un nombre entier:"))
chiffrement_cesar(chaine_de_caractere,cle)


