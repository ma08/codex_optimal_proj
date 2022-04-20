

n = int(input())
words = input().split(' ')

#print(words)

def abbreviation(words):
    """
    Returns the length of the text after abbreviation
    """
    length = 0
    i = 0
    while i < len(words):
        #print(words)
        if i+1 < len(words) and words[i] == words[i+1]:
            #print('i =', i)
            #print('i+1 =', i+1)
            #print('words[i]', words[i])
            #print('words[i+1]', words[i+1])
            #print('length =', length)
            #print('len(words[i]) =', len(words[i]))
            #print('len(words[i+1]) =', len(words[i+1]))
            #print('len(words[i]) + len(words[i+1]) =', len(words[i]) + len(words[i+1]))
            #print('len(words[i]) + len(words[i+1]) - 1 =', len(words[i]) + len(words[i+1]) - 1)
            #print('len(words[i]) + len(words[i+1]) - 2 =', len(words[i]) + len(words[i+1]) - 2)
            #print('len(words[i]) + len(words[i+1]) - 3 =', len(words[i]) + len(words[i+1]) - 3)
            length = length - len(words[i]) - len(words[i+1]) + 1
            words[i] = words[i][0].upper()
            del words[i+1]
            #print('length =', length)
            #print('i =', i)
            #print('i+1 =', i+1)
        else:
            length = length + len(words[i])
            #print('length =', length)
            i = i + 1
            #print('i =', i)
    return length

print(abbreviation(words))