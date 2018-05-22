# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:34:35 2018

@author: etudiant
"""
import QUESTION7       # nous importons le fichier dans lequel il y a la fonction qui nous intéresse, à savoir la fonction decaler
    

def chiffrement_cesar(chaine_de_caractere, cle):
    chiff = ""      #on a nommé cette variable pour pouvoir l'utiliser ensuite et elle vide parce qu'elle va se remplir au fur et à mesure que la chaine de caractères sera chiffrée
    for char in chaine_de_caractere:  #char permet de s'intéresser à chaque caractère
        chiff = chiff+QUESTION7.decaler(char,cle)  # comme on utilise la fonction decaler, il faut la précéder du nom du chier dans laquelle elle est suivie d'un point 
    print(chiff)
    return chiff

chaine_de_caractere = input("Veuillez saisir votre texte:")
cle = int(input("Veuillez saisir un nombre entier:"))
chiffrement_cesar(chaine_de_caractere,cle)


