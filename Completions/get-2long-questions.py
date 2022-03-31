# Get questions that are too long for Codex

import os
from nltk.tokenize import word_tokenize
import json

d1 = './train/sort-questions.txt_dir'
d2 = './train/search-questions.txt_dir'
d3 = './test/sort-questions.txt_dir'
d4 = './test/search-questions.txt_dir'
d5 = './train/intro-questions.txt_dir'
d6 = './test/intro-questions.txt_dir'
rootdirs = [d1, d2, d3, d4, d5, d6]
# 2920 is roughly 4000 tokens
word_lim = 2920 #1500
char_lim = word_lim * 4.7 # average word is 4.7 characters

def get2longqs(d, wl, cl):
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
				wcounts = [len(word_tokenize(s)) for s in sols if len(s) <= cl]
				max_sol_wc = max(wcounts) if wcounts else wl

			if q_nw + max_sol_wc >= wl:
				print(os.path.join(subdir, f))

for d in rootdirs:
	get2longqs(d, word_lim, char_lim)
	print()
