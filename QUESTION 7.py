# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:45:23 2018

@author: etudiant
"""

# La table ASCII/Unicode

#Question 7

caractere = input("Veuillez saisir une lettre:")
decalage = int(input("Veuillez saisir un nombre:")) 

def decaler(caractere, decalage):
    nombre = ord(caractere) + decalage
    print(chr(nombre))
    return chr(nombre)

decaler(caractere, decalage)
    
    

