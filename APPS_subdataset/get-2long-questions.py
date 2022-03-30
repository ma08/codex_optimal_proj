# Get questions that are too long for Codex

import os
from nltk.tokenize import word_tokenize
import json

d1 = './train/sort-questions.txt_dir'
d2 = './train/search-questions.txt_dir'
d3 = './test/sort-questions.txt_dir'
d4 = './test/search-questions.txt_dir'
rootdirs = [d1, d2, d3, d4]
word_lim = 1500 #2920

def get2longqs(d, wl):
	for subdir, dirs, files in os.walk(d):
		max_sol_wc = 0
		for f in dirs:
			qf = os.path.join(subdir, f, "question.txt")
			qc = open(qf, "r").read()
			q_nw = len(word_tokenize(qc))

			sf = os.path.join(subdir, f, "solutions.json")
			if os.path.exists(sf):
				sc = open(sf)
				sols = json.load(sc)
				wcounts = [len(word_tokenize(s)) for s in sols]
				max_sol_wc = max(wcounts)

			if q_nw + max_sol_wc >= wl:
				print("Question %s is too long" %(os.path.join(subdir, f)))

for d in rootdirs:
	get2longqs(d, word_lim)
	print()
