# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:45:23 2018

@author: etudiant
"""

# La table ASCII/Unicode

#Question 7

caractere = input("Veuillez saisir une lettre:")
decalage = int(input("Veuillez saisir un nombre:")) # int pour transformer le nombre en chaine de caractere (Python ne comprend que les chaines de caractere)
                                                    #str permet de prendre quelque chose comme une chaine de caractere aussi
def decaler(caractere, decalage):
    nombre = ord(caractere) + decalage
    print(chr(nombre))
    return chr(nombre)

decaler(caractere, decalage)
    
    

