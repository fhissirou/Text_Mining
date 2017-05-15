#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Stopword : python3 main.py -t Stopword -f ../input/data_no_stop.txt
Phrase : python3 main.py -t Stopword -f ../input/data_no_stop.txt
Nompropre : python3 main.py -t Nompropre -f ../input/data_no_stop.txt
Countword : python3 main.py -t Countword -f ../input/data_no_stop.txt
Préfixe : python3 main.py -t Préfixe -f ../input/data_no_stop.txt
Suffixe : python3 main.py -t Suffixe -f ../input/data_no_stop.txt
Synonyme :python3 main.py -t Synonyme -f ../input/data_no_stop.txt
Ngram : python3 main.py -t Ngram -f ../input/data_no_stop.txt
Entité nommées : python3 main.py -t NameEntity -f ../input/data_no_stop.txt
"""


import argparse
import sys
import os
import stopword
import nompropre
import sentenceword
import prefixeSuffixe
import synonyme
import ngramNameEntity



if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--type", dest="type", type=str, help="type de fonction:\
		'Stopword', 'Nompropre', 'Phrase', 'Countword', 'Prefixe', 'Suffixe', 'Synonyme', 'Ngram', 'NameEntity', 'All' ")
	parser.add_argument("-f", "--file", dest="file", help="nom du fichier d'entrée", metavar="FILE")
	args = parser.parse_args()

	if args.type =="Stopword":
		stopword.stopWords(args.file)
	if args.type =="Nompropre":
		nompropre.nomPropre(args.file)
	if args.type == "Phrase":
		sentenceword.sepPhrase(args.file)
	if args.type =="Countword":
		sentenceword.countWord(args.file)
	if args.type =="Prefixe":
		prefixeSuffixe.prefixe(args.file)
	if args.type =="Suffixe":
		prefixeSuffixe.suffixe(args.file)
	if args.type =="Synonyme":
		synonyme.synonymes(args.file)
	if args.type =="Ngram":
		ngramNameEntity.ngramsWord(args.file)
	if args.type =="NameEntity":
		ngramNameEntity.nameEntity(args.file)

	if args.type =="All":
		stopword.stopWords(args.file)
		nompropre.nomPropre(args.file)
		sentenceword.sepPhrase(args.file)
		sentenceword.countWord(args.file)
		prefixeSuffixe.prefixe(args.file)
		prefixeSuffixe.suffixe(args.file)
		synonyme.synonymes(args.file)
		ngramNameEntity.ngramsWord(args.file)
		ngramNameEntity.nameEntity(args.file)