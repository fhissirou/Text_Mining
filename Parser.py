#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.util import ngrams

class Parser:
	def __init__(self,filename):
		self.Infile= filename
		self.StrFileSeparateSentences= "Separate_sentences.xml"
		self.StrFileNomPropre="Nom_propre.txt"
		self.StrFileCountWord="Count_words.txt"
		self.StrFileNgramPreDebut="Ngram_prefixe_debut.txt"
		self.StrFileNgramPreFin="Ngram_prefixe_fin.txt"
		self.StrFileNgramWord="Ngram_words.txt"
		self.StrFileStopWords="stopwords.txt"
		self.StrFileSynonymes="Synonymes.txt"
		
		self.SeparateSentences(self.Infile, self.StrFileSeparateSentences)
		self.countWords(self.Infile, self.StrFileCountWord)
		self.nomPropre(self.Infile, self.StrFileNomPropre)
		self.ngram_prefixe_debut(self.StrFileCountWord, self.StrFileNgramPreDebut)
		self.ngram_prefixe_fin(self.StrFileCountWord, self.StrFileNgramPreFin)
		self.ngrams_word(self.Infile, self.StrFileNgramWord)
		self.synosymes(self.StrFileCountWord, self.StrFileSynonymes)

	def existe(self, word, l_word):
		for i in l_word:
			if word == i:
				return 1
		return 0

	def stopWords(self, contenu):
		
		fileStopwords= open(self.StrFileStopWords, encoding="utf-8", mode='r', errors="ignore")
		stopWords = fileStopwords.readlines()
		
		token = word_tokenize(contenu)
		tokenizer = WordPunctTokenizer()
		token = tokenizer.tokenize(contenu)
		
		filtered_sentence = []
		#Pour chaque mot de notre corpus
		for word in token:
			trouve = 0
			#Pour chaque mot de notre stopwords
			for wstop in stopWords:
				#On compare le mot du corpus avec stop en majuscule et miniscule
				wstop = wstop.replace("\n", "")

				if (word != wstop.lower()) and (word != wstop.upper()):
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
				filtered_sentence.append(word)
		#fermeture du fichier
		fileStopwords.close()
		#print(filtered_sentence)
		return filtered_sentence

	#Cette fonction separe le contenu du corpus en plusieurs phrases
	def SeparateSentences(self, strfileread, strfilesave):
		#La variable fileread contient le fichiers d'entrée c'est a dire le corpus
		#La variable filesave est le fichier de sauvergade
		fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")

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

	def countWords(self, strfileread, strfilesave):
		fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")

		content_file = fileread.read()
		#token = word_tokenize(content_file)
		token = self.stopWords(content_file)
		liste_word= []

		for word in token:

			if self.existe(word, liste_word) !=1:
				nb_word= 0
				#On compte le nombre d'occurence du mot
				for chaine_mt in token:
					if chaine_mt == word:
						nb_word += 1
				filesave.write(word+": "+str(nb_word)+"\n")
				liste_word.append(word)

		fileread.close()
		filesave.close()

	def nomPropre(self, strfileread, strfilesave):
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")
		fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		contenu = fileread.read()
		ma_liste="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lmot = word_tokenize(contenu)
		lcontenu = contenu.split("\n")
		listes_debut=[]
		for line in lcontenu:
			lline = word_tokenize(line)

			for mt in lline:
				if self.existe(mt, listes_debut) !=1:
					listes_debut.append(mt)
					val = mt[:1]
					if ma_liste.find(val) != -1:
						trouve = 0
						#On parcours le corpus pour chercher existance du mot en miniscule
						for i in lmot:
							#On verifie si c'est le mt est egale a i donc cela veut dire qu'il n'est pas un nom propre
							if mt.lower() == i:
								trouve = 1
								break
						#On verifie bien qu'il fait partie des noms prores		
						if trouve == 0:
							filesave.write("<NP>"+mt+"</NP>\n")
		fileread.close()
		filesave.close()



	def ngram_prefixe_debut(self, strfileread,strfilesave):
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")
		fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		content = fileread.readlines()
		ma_liste=[]
		#On affiche le ngram des lettres entre de 2 à 6
		for n in range (2,7):
			#On parcours le contenu du fichier text qui contient le nombre de caractère d'occurence
			for lg in content:
				#On separer les mots et les chiffres
				lg_split= lg.split(":")
				ligne = lg_split[0]

				if (len(ligne) -1 ) >= n:
					chaine1 = ''.join(ligne[:n])
					# on verifier que le mot n'est pas déjà aouté à la liste
					if not (chaine1  in ma_liste):
						#On ajoute le mot dans la liste
						ma_liste.append(chaine1)
						ma_liste2=[]
						#On parcours les autres mots qui ont le meme prefixe au debut du mot 
						for lign in content:
							lign_split= lign.split(":")
							ligne2 = lign_split[0]	
							if not (ligne2  in ma_liste2):
								chaine2 = ''.join(ligne2[:n])
								#On verifi bien que les prefixe sont les même
								if chaine1 == chaine2:
									ma_liste2.append("".join(ligne2))
						#On sauvergarde dans le fichier
						filesave.write(chaine1+ " = ["+",".join(ma_liste2)+"]\n")
		filesave.close()
		fileread.close()

	def ngram_prefixe_fin(self, strfileread,strfilesave):
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")
		fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		content = fileread.readlines()
		ma_liste=[]
		#On affiche le ngram des lettres entre de 2 à 6
		for n in range (2,7):
			#On parcours le contenu du fichier text qui contient le nombre de caractère d'occurence
			for lg in content:
				#On separer les mots et les chiffres
				lg_split= lg.split(":")
				ligne = lg_split[0]

				if (len(ligne) -1 ) >= n:
					chaine1 = ''.join(ligne[-n:])
					# on verifier que le mot n'est pas déjà aouté à la liste
					if not (chaine1  in ma_liste):
						#On ajoute le mot dans la liste
						ma_liste.append(chaine1)
						ma_liste2=[]
						#On parcours les autres mots qui ont le meme prefixe à partid de la fin du mot 
						for lign in content:
							lign_split= lign.split(":")
							ligne2 = lign_split[0]	
							if not (ligne2  in ma_liste2):
								chaine2 = ''.join(ligne2[-n:])
								#On verifi bien que les prefixe sont les même
								if chaine1 == chaine2:
									ma_liste2.append("".join(ligne2))
						#On sauvergarde dans le fichier
						filesave.write(chaine1+ " = ["+",".join(ma_liste2)+"]\n")
		filesave.close()
		fileread.close()


	def ngrams_word(self, strfileread, strfilesave):
		#La variable fileread contient le fichiers d'entrée c'est a dire le corpus
		#La variable filesave est le fichier de sauvergade
		fileread = open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")

		#Lecture du corpus
		content_file = fileread.read()
		#sent_tokenize permet de separer un corpus en plusieurs phrases
		token= sent_tokenize(content_file)
		tokenizer = WordPunctTokenizer()
		#On parcours chaque mot
		for line in token:
			l=[]
			stp_line= self.stopWords(line)
			for n in range(2, 7):
				s = []
				for ngram in ngrams(stp_line, n):
					chaine =', '.join(str(i) for i in ngram)
					filesave.write("["+chaine+"]\n")

		fileread.close()
		filesave.close()


	def synosymes(self, strfileread,strfilesave):

		filesave = open(strfilesave, encoding="utf-8", mode='w+', errors="ignore")
		fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
		content = fileread.readlines()
		ma_liste=[]

		for lg in content:
			#On separer les mots et les chiffres
			lg_split= lg.split(":")
			chaine = lg_split[0]

			l_elem=[]
			for synset in wn.synsets(chaine, lang='fra'):
				params = synset.lemma_names(lang='fra')

				for word in params:
					if self.existe(word, l_elem) !=1:
						if word != chaine:
							l_elem.append(word)
			if len(l_elem) > 0:
				filesave.write(chaine+ " = ["+",".join(l_elem)+"]\n\n")

		filesave.close()
		fileread.close()




if __name__ == "__main__":
	

	if(len(sys.argv) == 1):
		print("manque de paramètre")
		exit(0)
	Parser(sys.argv[1])
