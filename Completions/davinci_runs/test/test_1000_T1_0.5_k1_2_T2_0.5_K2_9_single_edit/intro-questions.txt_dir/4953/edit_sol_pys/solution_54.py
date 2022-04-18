

import fileinput

def main():
    # read input
    N = int(input())
    characters = {}
    for i in range(N):
        line = input().split()
        name = line[0]
        lang = line[1]
        chars = set([lang])
        for j in range(2, len(line)):
            chars.add(line[j])
        characters[name] = chars
    # calculate the set of characters that can converse with everyone
    conversations = []
    for name in characters.keys():
        chars = characters[name]
        for other in characters.keys():
            if name == other:
                continue
            if len(chars.intersection(characters[other])) == 0:
                conversations.append((name, other))
    # find the set of characters that should be removed
    remove = set()
    for name, other in conversations:
        remove.add(name)
        remove.add(other)
    # print the result
    print(len(remove))

if __name__ == '__main__':
    main()
