# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:06:42 2018

@author: etudiant
"""
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

def compter_occurences(espace, chaine):
    compteur = 0
    for i in range(len(chaine)):
        if chaine[i] == espace:
            compteur += 1
            A = 1 + compteur
    print(A)
    return A


compter_occurences(" ", chaine)

