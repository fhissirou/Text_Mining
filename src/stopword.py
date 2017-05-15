#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from nltk.tokenize import word_tokenize

def stopWords(inputdata):
		
	fileStopwords= open("../input/stopwords.txt", encoding="utf-8", mode='r', errors="ignore")
	fileread= open(inputdata, encoding="utf-8", mode='r', errors="ignore")
	filesave= open("../input/data_no_stop.txt",encoding="utf-8", mode='w+', errors="ignore")

	stopWords = fileStopwords.readlines()
	contenu= fileread.read() 
	
	#tokenizer = WordPunctTokenizer()
	#token = tokenizer.tokenize(contenu)
	token= word_tokenize(contenu)
	filtered_sentence = []
	full_text=""
	#Pour chaque mot de notre corpus
	for word in token:
		trouve = 0
		#Pour chaque mot de notre stopwords
		for wstop in stopWords:
			#On compare le mot du corpus avec stop en majuscule et miniscule
			wstop = wstop.replace("\n", "")

			if (word != wstop.lower()) and (word != wstop.upper()) and (word.isdigit()!=True):
				#On cherche s'il ya l'équivalent du mot avec un caractère commençant par une lettre majuscule 
				#ex: Les ou La
				tmp = wstop[:1].upper()
				tmp+= wstop[1:].lower()
				#On verifie l'équivalence
				if word == tmp:
					trouve = 1
					break
			else: 
				trouve= 1
				break
		#On verifie que le mot n'est pas dans la liste de stop alors on ajoute a la variable filtered_sentence
		if trouve == 0:
			full_text+=word+" "
	

	filesave.write(full_text)
	
	#fermeture du fichier
	fileStopwords.close()
	fileread.close()
	filesave.close()




