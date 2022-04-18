

"""
We need to find the minimum distance between two people who speak the same language.

This can be done by keeping track of the last positions of each language.

We keep track of the last position of each language, and the distance between the current position and the last position of each language.

The minimum distance is the minimum of these distances.
"""

n = int(input())

languages = list(map(int, input().split()))  # split() splits a string into a list of words

last_position = {}  # create an empty dictionary

min_distance = n

for i in range(n):
    if languages[i] in last_position:  # if the language is in the dictionary
        min_distance = min(min_distance, i - last_position[languages[i]])  # update the minimum distance
    last_position[languages[i]] = i  # add the new language to the dictionary

print(min_distance)
