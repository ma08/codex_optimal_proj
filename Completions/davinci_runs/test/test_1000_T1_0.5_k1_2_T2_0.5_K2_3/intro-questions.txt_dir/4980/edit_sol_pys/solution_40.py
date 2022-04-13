
N = int(input())  # get the number of input words

count = 0
for i in range(N):
    word = input()
    word = word.lower()  # convert all the words to lower case
    if "pink" in word or "rose" in word:
        count += 1

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter") 
