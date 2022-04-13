
# Solution

# The solution is based on the following observation
# For each word in the dictionary, the number of ways to translate the sentence is the product of the number of ways to translate the word that comes directly before that word in the sentence and the number of ways to translate the word itself.

# The number of ways to translate a word is simply the number of times that word appears in the dictionary, if it is incorrect, and one if it is correct.

# Therefore, we can iterate over the sentence from left to right, keeping track of the number of ways to translate each word that appears in the sentence. Then, for each word in the dictionary, we multiply the number of ways to translate the word that comes directly before that word in the sentence by the number of ways to translate the word itself and add the result to the number of ways to translate the current word in the sentence.

# The number of ways to translate a word is simply the number of times that word appears in the dictionary, if it is incorrect, and one if it is correct.

# In order to keep track of the number of ways to translate each word that appears in the sentence, we use a dictionary mapping the words in the sentence to the number of ways to translate them. We initialize this dictionary to map each word in the sentence to one, since there is always at least one way to translate a word: correctly.

# We also need to keep track of the number of ways to translate the current word in the sentence. To do this, we keep track of the current word in the sentence, and we initialize the number of ways to translate the current word in the sentence to one.

# Then, for each word in the dictionary, we multiply the number of ways to translate the word that comes directly before that word in the sentence by the number of ways to translate the word itself and add the result to the number of ways to translate the current word in the sentence. The number of ways to translate the word that comes directly before that word in the sentence is the value in the dictionary corresponding to that word. The number of ways to translate the word itself is one if the word is correct and the number of times that word appears in the dictionary if the word is incorrect.

#After we have processed the entire dictionary, we output the number of ways to translate the current word in the sentence followed by “correct” and the number of ways to translate the current word in the sentence followed by “incorrect”.

#To solve the problem, we first read in the sentence and the dictionary. We keep track of the current word in the sentence and the number of ways to translate the current word in the sentence. We also keep track of the number of ways to translate each word that appears in the sentence in a dictionary.

n = int(input())
sentence = input().split()
m = int(input())

curr = sentence[0]
num_correct = 1
num_incorrect = 0
num_ways = {curr: 1}

#Then, we iterate over the dictionary. For each word in the dictionary, we multiply the number of ways to translate the word that comes directly before that word in the sentence by the number of ways to translate the word itself and add the result to the number of ways to translate the current word in the sentence.

for i in range(m):
    dutch, english, correct = input().split()
    if dutch == curr:
        if correct == "correct":
            num_correct += num_incorrect
        else:
            num_incorrect += num_correct
    else:
        curr = dutch
        num_correct = num_ways[curr]
        num_incorrect = 0
        for word in sentence:
            if word == curr:
                num_incorrect += 1

#Finally, we output the number of ways to translate the current word in the sentence followed by “correct” and the number of ways to translate the current word in the sentence followed by “incorrect”.

print(num_correct, "correct")
print(num_incorrect, "incorrect")
