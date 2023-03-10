#!/usr/bin/python3
# -*- coding : utf-8  -*-

import re
chaine = input ("Votre nombre : ") # Demande à l ‘utilisateur  de saisir un nombre

if (re.search(r"^[0-9]+$", chaine)):  # Expression regulière au moins un chiffre
    print ("la chaine est bien un nombre")
else:
    print ("la chaine saisie n'est pas un nombre") 