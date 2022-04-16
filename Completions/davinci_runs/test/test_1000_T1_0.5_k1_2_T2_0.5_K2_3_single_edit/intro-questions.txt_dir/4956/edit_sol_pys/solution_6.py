
# Read input
sentence = input()

# Split sentence into words and count
words = sentence.split()
num_words = len(words)

# Count number of words with ae
num_ae = 0
for word in words:
    if "ae" in word:
        num_ae += 1

# Print correct output
if num_ae/num_words >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
