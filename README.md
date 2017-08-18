# Text Mining
---

|               Fodé HISSIROU               |
---


##  Objectif

L’objectif de ce projet consiste à connaître l’architecture de base des systèmes
du traitement automatique du langage naturel de manière à pouvoir concevoir un 
système selon les besoins spécifiques. Il consiste également de découvrir certain
outils linguistiques comme Natural Language Toolkit qui est basé sur python et 
d’appliquer des différentes méthodes de fouilles de données a des données textuelles.

## 1. Introduction

Ce programme est composé de plusieurs fonctionnalités différentes comme la séparation du corpus
en phrases, la suppression des stopword, l’occurrence des mots, la détection des noms propres, le
préfixe d’un mots, le suffixe d’un mots et les synonymes d’un mot. L’ensemble des scripts se trouve
dans le repertoire src et est repartie sur plusieurs fichiers différents.

#### - Pour lancer le programme par exemple:
    - Stopword : python3 main.py -t Stopword -f ../input/data_no_stop.txt
    - Phrase : python3 main.py -t Stopword -f ../input/data_no_stop.txt
    - Nompropre : python3 main.py -t Nompropre -f ../input/data_no_stop.txt
    - Countword : python3 main.py -t Countword -f ../input/data_no_stop.txt
    - Préfixe : python3 main.py -t Préfixe -f ../input/data_no_stop.txt
    - Suffixe : python3 main.py -t Suffixe -f ../input/data_no_stop.txt
    - Synonyme :python3 main.py -t Synonyme -f ../input/data_no_stop.txt
    - Ngram : python3 main.py -t Ngram -f ../input/data_no_stop.txt
    - Entité nommées : python3 main.py -t NameEntity -f ../input/data_no_stop.txt

## 2. La séparation du corpus en Phrase

La fonction SeparateSentences() permet de faire une séparation du corpus en phrase. Pour cela on
lui donne deux fichiers en paramètre : le premier est le nom du fichier du corpus d’entrée et le
second est le fichier de sauvegarde. Elle utilise principalement la fonction sent_tokenize() de la
librarie nltk pour faire une séparation du texte en une liste de phrase. À l'aide d’une boucle je
parcours chaque élément de la liste pour ajouter le balise <p> au début de la phrase et </p> à la fin
de la phrase. Cette tache se fait juste avant le sauvegarde des phrases dans un fichier. La figure ci-
dessous représente un exemple du contenu du fichier de separate_sentences.xml

![](images/image01.png)


