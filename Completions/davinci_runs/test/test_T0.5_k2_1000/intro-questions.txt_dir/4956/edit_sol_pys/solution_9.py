

import sys

# Function that returns true if a string contains the substring "ae"
def contains_ae(string):
    if string.find("ae") != -1:
        return True
    else:
        return False

# Read input
line = sys.stdin.readline()

# Split input into list of words
words = line.split()

# Count number of words with "ae"
num_words_with_ae = 0
for word in words:
    if contains_ae(word):
        num_words_with_ae += 1

# Calculate percentage of words with "ae"
percentage_with_ae = float(num_words_with_ae) / float(len(words))

if percentage_with_ae >= 0.4:
    print("dae ae ju traeligt va") # då är du träligt va
else:
    print("haer talar vi rikssvenska") # här talar vi rikssvenska
