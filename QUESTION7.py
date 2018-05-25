# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:45:23 2018

@author: etudiant
"""

# La table ASCII/Unicode 

#Question 7 - CE CODE NE MARCHE QUE SUR PYTHON 

caractere = input("Veuillez saisir une lettre:")
decalage = int(input("Veuillez saisir un nombre:")) # int pour transformer le nombre en chaine de caractere (Python ne comprend que les chaines de caractere)
                                                    #str permet de prendre quelque chose comme une chaine de caractere aussi
def decaler(caractere, decalage):
    nombre = ord(caractere) + decalage # la fonction ord permet d'attribuer à un caractère un numéro grâce aux tables ASCII et Unicode
    print(chr(nombre)) # l fonction chr permet de retrouver un caractère à partir de son numéro
    return chr(nombre)

decaler(caractere, decalage)
    
    

