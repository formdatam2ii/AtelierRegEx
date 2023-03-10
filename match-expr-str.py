#!/usr/bin/python3
# -*- coding : utf-8  -*-

import re


# Lecture de l'ensemble des expressions régulières

f = open ("regex.txt","r")
regexs= f.readlines()
f.close()

# Lecture de l'ensemble des chaînes à analyser régulières

f = open ("chaines.txt","r")
lignes= f.readlines()
f.close()

# print ("Les regex :  \n \n" + regexs)
# print ("\n Les lignes :  \n \n" + lignes)


for phrase in lignes :
    # on supprime le caractère de fin de ligne
    str = phrase.rstrip('\r\n')
    print ("Les phrase :  \n " + phrase)
    for reg in regexs :
        print ("Les reg :  \n " + reg)
        # on supprime le caractère de fin de ligne de la regex
        regex = reg.rstrip('\r\n')
        
        # Test de l'expression régulière et de la chaine
        if re.search(regex,str) :
            print ('"' +"\" correspond à "+regex)