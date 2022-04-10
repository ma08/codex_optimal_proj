

import sys

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.suffix_link = None
        self.parent = None
        self.end_pos = -1
        self.end_pos_in_parent = -1
        self.depth = -1

class SuffixTree:
    def __init__(self, s):
        s += '$'
        self.root = Node('')
        self.root.depth = 0
        self.root.end_pos = -1
        self.s = s
        self.n = len(s)

    def _add_char(self, node, i, depth):
        node.children[self.s[i]] = Node(self.s[i])
        node.children[self.s[i]].parent = node
        node.children[self.s[i]].depth = depth
        node.children[self.s[i]].end_pos = i
        node.children[self.s[i]].end_pos_in_parent = i

    def _get_suffix_link(self, node):
        if node.suffix_link is not None:
            return node.suffix_link
        if node == self.root or node.parent == self.root:
            node.suffix_link = self.root
            return self.root
        node.suffix_link = self.get_suffix_link(node.parent.suffix_link, node.end_pos_in_parent)
        return node.suffix_link

    def get_suffix_link(self, node, i):
        if i == -1:
            return self.root
        if self.s[i] in node.children:
            return node.children[self.s[i]]
        if node == self.root:
            return self.root
        return self.get_suffix_link(node.suffix_link, i)

    def build(self):
        for i in range(self.n):
            node = self.root
            for j in range(i, self.n):
                if self.s[j] in node.children:
                    node = node.children[self.s[j]]
                    continue
                self._add_char(node, j, j - i + 1)
                node = node.children[self.s[j]]
                sl = self._get_suffix_link(node)
                while sl != self.root:
                    if self.s[i + sl.depth] in sl.children:
                        node.suffix_link = sl.children[self.s[i + sl.depth]]
                        break
                    sl = sl.suffix_link
                if sl == self.root:
                    node.suffix_link = self.root

    def get_leaves(self, node):
        res = []
        if len(node.children) == 0:
            res.append(node)
        else:
            for child in node.children.values():
                res += self.get_leaves(child)
        return res

    def get_leaves_count(self, node):
        res = 0
        if len(node.children) == 0:
            res += 1
        else:
            for child in node.children.values():
                res += self.get_leaves_count(child)
        return res

def get_min_text_length(s):
    st = SuffixTree(s)
    st.build()
    leaves = st.get_leaves(st.root)
    leaves_count = st.get_leaves_count(st.root)
    if leaves_count == 1:
        return len(s)
    leaves = sorted(leaves, key=lambda x: x.depth, reverse=True)
    for i in range(len(leaves) - 1):
        if leaves[i].depth == leaves[i + 1].depth:
            return len(s) - leaves[i].depth * 2
    return len(s)

def main():
    n = int(input())
    s = input().split()
    s = ' '.join(s)
    print(get_min_text_length(s))

if __name__ == '__main__':
    main()