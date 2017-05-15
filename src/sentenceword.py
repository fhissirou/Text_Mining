#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer


def dejaVue(word, l_word):
	for i in l_word:
		if word == i:
			return 1
	return 0


def sepPhrase(strfileread):
	#La variable fileread contient le fichiers d'entrée c'est a dire le corpus
	#La variable filesave est le fichier de sauvergade
	fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	filesave = open("../output/sepPhrases.xml", encoding="utf-8", mode='w+', errors="ignore")

	#Lecture du corpus
	content_file = fileread.read()
	#sent_tokenize permet de separer un corpus en plusieurs phrases
	token= sent_tokenize(content_file)
	#On parcours chaque mot
	for line in token:
		#Avec la conftion word_tokenize on separe le corpus en mot cela est nécessaire pour supprimer \t \n et bien autres types
		filesave.write("<p>" + " ".join(word_tokenize(line)) + "</p>\n\n")

	fileread.close()
	filesave.close()

def countWord(strfileread):
	fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	filesave = open("../output/countWord.xml", encoding="utf-8", mode='w+', errors="ignore")

	content_file = fileread.read()

	tokenizer = WordPunctTokenizer()
	token = tokenizer.tokenize(content_file)

	liste_word= []

	full_text=""
	for word in list(set(token)):

		if dejaVue(word, liste_word) !=1:
			if len(word) >2:
				nb_word= 0
				#On compte le nombre d'occurence du mot
				for chaine_mt in token:
					if chaine_mt == word:
						nb_word += 1
				full_text+="<p>\n\t<word>"+word+"</word>\n\t<nb>"+str(nb_word)+"</nb>\n</p>\n"

				liste_word.append(word)
	filesave.write(full_text)
	fileread.close()
	filesave.close()
