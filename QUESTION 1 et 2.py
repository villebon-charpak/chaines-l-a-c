# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:06:42 2018

@author: etudiant
"""

chaine = input("Veuillez saisir du texte")


def compter_occurences(caractere, chaine):
    compteur = 0
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            compteur += 1
    print(compteur)
    return compteur


compter_occurences("u", chaine)