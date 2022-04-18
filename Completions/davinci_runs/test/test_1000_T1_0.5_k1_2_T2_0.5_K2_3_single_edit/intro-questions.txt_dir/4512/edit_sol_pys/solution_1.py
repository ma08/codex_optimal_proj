

# TODO: implement using a Trie instead of a hashmap, or just use Python's built-in Trie

class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr.children[letter].count += 1
            curr = curr.children[letter]
        return curr

    def find(self, word):
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return 0
        return curr.count


def main():
    s = input()
    q = int(input())

    trie = Trie()
    for letter in s:
        trie.add(letter)

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            trie.add(query[2])
        elif query[0] == '2':
            print(trie.find(s[int(query[1]) - 1: int(query[2])]))


if __name__ == '__main__':
    main()
