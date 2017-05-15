#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from nltk.tokenize import word_tokenize
import sentenceword

def nomPropre(strfileread):
	filesave = open("../output/NomPropre.xml", encoding="utf-8", mode='w+', errors="ignore")
	fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	contenu = fileread.read()
	ma_liste="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lmots = word_tokenize(contenu)
	lmots= list(set(lmots))
	lmots.sort()
	lcontenu = contenu.split("\n")
	listes_debut=[]
	full_text=""
	for line in lcontenu:
		lline = word_tokenize(line)

		for mt in lline:
			if sentenceword.dejaVue(mt, listes_debut) !=1:
				listes_debut.append(mt)
				val = mt[:1]
				if ma_liste.find(val) != -1:
					trouve = 0
					#On parcours le corpus pour chercher existance du mot en miniscule
					for i in lmots:
						#On verifie si c'est le mt est egale a i donc cela veut dire qu'il n'est pas un nom propre
						if mt.lower() == i:
							trouve = 1
							break
					#On verifie bien qu'il fait partie des noms prores      
					if trouve == 0:
						full_text+="<nomPropre>"+mt+"</nomPropre>\n"
	
	filesave.write(full_text)
	fileread.close()
	filesave.close()


