#!/usr/bin/python3
# -*- coding : utf-8  -*-

import re
saisie = input ("Votre immatriculation ? : ") # Demande à l ‘utilisateur  de saisir un nombre
immat  = saisie.rstrip('\r\n')
if (re.search(r"[A-HJ-NP-TV-Z]{2}[\s-]{0,1}[0-9]{3}[\s-]{0,1}[A-HJ-NP-TV-Z]{2}|[0-9]{2,4}[\s-]{0,1}[A-Z]{1,3}[\s-]{0,1}[0-9]{2}", immat)):  # Expression regulière au moins un chiffre
    print ("\""+ immat +"\" est une plaque mineralogique")
else:
    print ("\""+ immat +"\" n'est pas une plaque mineralogique")