# Get questions that are too long for Codex

import os
from nltk.tokenize import word_tokenize

rootdir1 = './train/sort-questions.txt_dir'
rootdir2 = './train/search-questions.txt_dir'
rootdir3 = './test/sort-questions.txt_dir'
rootdir4 = './test/search-questions.txt_dir'

word_lim = 1500

for subdir, dirs, files in os.walk(rootdir1):
	for f in files:
		if f == "question.txt":
			fp = os.path.join(subdir, f)
			fc = open(fp, "r").read()
			nwords = len(word_tokenize(fc))
			if nwords >= word_lim:
				print("File %s has %s words" %(fp, nwords))

print()

for subdir, dirs, files in os.walk(rootdir2):
	for f in files:
		if f == "question.txt":
			fp = os.path.join(subdir, f)
			fc = open(fp, "r").read()
			nwords = len(word_tokenize(fc))
			if nwords >= word_lim:
				print("File %s has %s words" %(fp, nwords))

print()

for subdir, dirs, files in os.walk(rootdir3):
	for f in files:
		if f == "question.txt":
			fp = os.path.join(subdir, f)
			fc = open(fp, "r").read()
			nwords = len(word_tokenize(fc))
			if nwords >= word_lim:
				print("File %s has %s words" %(fp, nwords))

print()

for subdir, dirs, files in os.walk(rootdir4):
	for f in files:
		if f == "question.txt":
			fp = os.path.join(subdir, f)
			fc = open(fp, "r").read()
			nwords = len(word_tokenize(fc))
			if nwords >= word_lim:
				print("File %s has %s words" %(fp, nwords))
