#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer

import sentenceword




def prefixe(strfileread):
	filesave = open("../output/prefixes.xml", encoding="utf-8", mode='w+', errors="ignore")
	fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	#content = fileread.read()
	lmots = word_tokenize(fileread.read())
	lmots = list(set(lmots))
	lmots.sort()
	lprefixe=[]

	#On affiche le ngram des lettres entre de 2 à 6
	for n in range (3,6):
		full_text=""
		#On parcours le contenu du fichier text
		for mot in lmots:
			if (len(mot) -1 ) >= n:
				chaine1 = ''.join(mot[:n])
				# on verifier que le mot n'est pas déjà ajouté à la liste
				if sentenceword.dejaVue(chaine1, lprefixe) !=1:
					#On ajoute le mot dans la liste
					lprefixe.append(chaine1)
					lprefixe2=[]
					#On parcours les autres mots qui ont le meme prefixe au debut du mot 
					for mot2 in lmots:
						if not (mot2  in lprefixe2):
							chaine2 = ''.join(mot2[:n])
							#On verifi bien que les prefixe sont les même
							if (chaine1.lower() == chaine2.lower()) or (chaine1.upper() == chaine2.upper()):
								lprefixe2.append("".join(mot2))
					#On sauvergarde dans le fichier
					full_text+="<prefixes>\n\t<radical>"+chaine1+"</radical>\n\t<liste>"+", ".join(lprefixe2)+"</liste>\n</prefixes>\n"
	
		if full_text != "":
			filesave.write(full_text)
	filesave.close()
	fileread.close()






def suffixe(strfileread):
	filesave = open("../output/suffixes.xml", encoding="utf-8", mode='w+', errors="ignore")
	fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	lmots = word_tokenize(fileread.read())
	lmots= list(set(lmots))
	lmots.sort()
	lsuffixe=[]
	
	#On affiche le ngram des lettres entre de 2 à 6
	for n in range (3,6):
		full_text=""
		#On parcours le contenu du fichier text
		for mot in lmots:
			if (len(mot) -1 ) >= n:
				chaine1 = ''.join(mot[-n:])
				# on verifier que le mot n'est pas déjà ajouté à la liste
				if sentenceword.dejaVue(chaine1, lsuffixe) !=1:
					#On ajoute le mot dans la liste
					lsuffixe.append(chaine1)
					lsuffixe2=[]
					#On parcours les autres mots qui ont le meme prefixe au debut du mot 
					for mot2 in lmots:
						if not (mot2  in lsuffixe2):
							chaine2 = ''.join(mot2[-n:])
							#On verifi bien que les prefixe sont les même
							if (chaine1.lower() == chaine2.lower()) or (chaine1.upper() == chaine2.upper()):
								lsuffixe2.append("".join(mot2))
					#On sauvergarde dans le fichier
					full_text+="<suffixes>\n\t<radical>"+chaine1+"</radical>\n\t<liste>"+", ".join(lsuffixe2)+"</liste>\n</suffixes>\n"
		
		if full_text != "":
			filesave.write(full_text)
	filesave.close()
	fileread.close()



"""
def ngram_prefixe_fin(self, strfileread,strfilesave):
	filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")
	fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	content = fileread.readlines()
	lsuffixe=[]
	#On affiche le ngram des lettres entre de 2 à 6
	for n in range (2,7):
		#On parcours le contenu du fichier text qui contient le nombre de caractère d'occurence
		for lg in content:
			#On separer les mots et les chiffres
			lg_split= lg.split(":")
			ligne = lg_split[0]

			if (len(ligne) -1 ) >= n:
				chaine1 = ''.join(ligne[-n:])
				# on verifier que le mot n'est pas déjà ajouté à la liste
				#if not (chaine1  in lsuffixe):
				if sentenceword.dejaVue(chaine1, lsuffixe) !=1:
					#On ajoute le mot dans la liste
					lsuffixe.append(chaine1)
					lsuffixe2=[]
					#On parcours les autres mots qui ont le meme prefixe à partid de la fin du mot 
					for lign in content:
						lign_split= lign.split(":")
						ligne2 = lign_split[0]  
						if not (ligne2  in lsuffixe2):
							chaine2 = ''.join(ligne2[-n:])
							#On verifi bien que les prefixe sont les même
							if chaine1 == chaine2:
								lsuffixe2.append("".join(ligne2))
					#On sauvergarde dans le fichier
					filesave.write(chaine1+ " = ["+",".join(lsuffixe2)+"]\n")
	filesave.close()
	fileread.close()

"""