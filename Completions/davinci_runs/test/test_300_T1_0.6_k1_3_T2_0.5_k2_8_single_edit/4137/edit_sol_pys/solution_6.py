
import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i","--input",required=True,help="input file")
    parser.add_argument("-o","--output",required=True,help="output file")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    with open(args.input,'r') as infile, open(args.output,'w') as outfile:
        for line in infile:
            outfile.write(line)

if __name__ == "__main__":
    main()
