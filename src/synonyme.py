#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import wordnet as wn
import sentenceword



def synonymes(strfileread):
	full_text=""
	filesave = open("../output/synonymes.xml", encoding="utf-8", mode='w+', errors="ignore")
	fileread= open(strfileread, encoding="utf-8", mode='r', errors="ignore")
	ma_liste=[]
	lmots = word_tokenize(fileread.read())
	lmots= list(set(lmots))
	lmots.sort()
	for mt in lmots:
		l_elem=[]
		for synset in wn.synsets(mt, lang='fra'):
			params = synset.lemma_names(lang='fra')

			for word in params:
				if sentenceword.dejaVue(word, l_elem) !=1:
					if word != mt:
						l_elem.append(word)
		if len(l_elem) > 0:
			full_text+="<synonymes>\n\t<word>"+mt+"</word>\n\t<liste>"+", ".join(l_elem)+"</liste>\n</synonymes>\n\n"
		

	filesave.write(full_text)

	filesave.close()
	fileread.close()