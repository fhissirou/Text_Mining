#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import word_tokenize
import sentenceword
from collections import Counter
import re

def ngramsWord(strfileread):
	#La variable fileread contient le fichiers d'entrée c'est a dire le corpus
	#La variable filesave est le fichier de sauvergade
	fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	filesave = open("../output/NgramWord.txt", encoding="utf-8", mode='w+', errors="ignore")

	#Lecture du corpus
	contenu = fileread.read()
	#sent_tokenize permet de separer un corpus en plusieurs phrases
	liste_lines= sent_tokenize(contenu)
	tokenizer = WordPunctTokenizer()
	
	#On parcours chaque mot
	full_text=""
	ma_liste=[]
	regex = re.compile("[,;!.?]")
	for n in range(2,7):

		for line in liste_lines:
			line = regex.sub("", line)
			token = tokenizer.tokenize(line)
			chaine="{"
			for gram in ngrams(token, n):
				chaine +="("+", ".join(gram)+"): "+str(n)+", "
				ma_liste.append(gram)
			chaine+="}\n\n"
			filesave.write(chaine)
		#return ma_liste
	filesave.close()
	fileread.close()
	return ma_liste



def nameEntity(strfileread):

	#lngrams = ngramsWord(strfileread)
	#La variable filesave est le fichier de sauvergade
	fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	filesave = open("../output/NameEntity.txt", encoding="utf-8", mode='w+', errors="ignore")
	filestopword = open("../input/stopwords.txt")

	stopword = word_tokenize(filestopword.read())
	liste_lines= sent_tokenize(fileread.read())
	tokenizer = WordPunctTokenizer()

	regex1 = re.compile(r"(z|s|i|e|t)+(-je|-tu|-il|-elle|-nous|-vous|-ils|-elles)")
	regex2 = re.compile(r"(l'|L'|c'|C'|d'|D'|s'|S'|qu'|n'|N'|j'|J')[a-z]")
	regex3 = re.compile(r"(?:[,;!?«»:])")
	regex4= re.compile(r"[A-Z]")

	lngrams=[]
	for n in range(2,4):
		for line in liste_lines:
			line = line.replace("--","")
			line = regex3.sub("", line)

			#token = tokenizer.tokenize(line)
			token = word_tokenize(line)
			for gram in ngrams(token, n):
				lngrams.append(" ".join(gram))
	full_text=""
	for gram in list(set(lngrams)):
		val =0
		if regex4.findall(str(gram)):
			regex1.sub("",str(gram))
			regex2.sub("", str(gram))
			for i in lngrams:
				if i == gram:
					val +=1
				if val >= 3:
					filesave.write(str(gram)+"\n")
					print(gram)
					break

	filesave.close()
	fileread.close()
	filestopword.close()
