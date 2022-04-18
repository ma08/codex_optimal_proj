

# TODO: implement using a Trie instead of a hashmap

class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr.children[char].count += 1
            curr = curr.children[char]
        return curr

    def find(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return 0
        return curr.count


def main():
    s = input()
    q = int(input())

    trie = Trie()
    for char in s:
        trie.add(char)

    for _ in range(q):
        query = input().split(' ')
        if query[0] == '1':
            trie.add(query[2])
        elif query[0] == '2':
            print(trie.find(s[int(query[1]) - 1: int(query[2])]))


if __name__ == '__main__':
    main()
