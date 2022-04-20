import os
import json
import sys

def convert(input_dir):
	sols = []
	for filename in os.listdir(input_dir):
		fname = os.fsdecode(filename)
		f = os.path.join(input_dir, filename)
		if fname.endswith(".py"):
			pyfile = open(f).read()
			sols.append(pyfile)

	out = os.path.join(input_dir, "codex_solutions.json")
	with open(out, "w") as outfile:
		json.dump(sols, outfile)

if __name__ == "__main__":
	input_dir = sys.argv[1] # ./2366/best/
	convert(input_dir)
