

# import sys

# def main():
#     words = sys.stdin.readline().strip().split() #get input from user
#     phrase = set()
#     for word in words:
#         if word in phrase:
#             print('no')
#             return
#         phrase.add(word)
#     print('yes')

# if __name__ == '__main__':
#     main()

def main(input):
    words = input.strip().split() #get input from user
    phrase = set() #create set to store unique words
    for word in words: #iterate through words
        if word in phrase: #if word is already in set
            return False #return false
        phrase.add(word) #add word to set
    return True #return true
