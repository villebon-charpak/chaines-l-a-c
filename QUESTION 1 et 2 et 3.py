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

def compter_mots(chaine):
    if chaine == '': # si la chaine est vide, il y a 0 mot
        return 0     #garde en mémoire le 0
    else :
       compteur = compter_occurences(' ', chaine)
       compteur = 1 + compteur
       print(compteur)
       return compteur


compter_occurences(" ", chaine)

##QUESTION 3 - NIVEAU 2

chaine = input("Veuillez saisir du texte\n")    #\n veut dire retour à la ligne 


def compter_mot(mot, chaine):
    compteur = 0
    for i in range(len(chaine)):
        if chaine[i:i+3] == mot:                #Pour compter le nombre de fois qu'apparait le lol, on applique la lecture de 3 lettres en 3 lettres grâce à [i:i+3], et ne pas poublier qu'en Python , on applique une borne supérieure stricte et surtout qu'on ajoute un +1 à notre borne
            compteur += 1
    print(compteur)
    return compteur

print(compter_mot("lol", chaine))               #Ne pas oublier à définir notre x et la chaine (le y) 
