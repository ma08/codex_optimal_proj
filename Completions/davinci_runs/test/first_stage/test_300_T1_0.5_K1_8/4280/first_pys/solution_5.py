

# SOLUTION
# We can use DFS to find the number of children of each node. 
# We will start with the root node. The root node has children, so it is not good. 
# Then we will assign the first company to all its children. 
# Then we will do the same for each of those children, assigning the second company to all its children. 
# We will continue this until we have no more children. 
# We will then go back up the tree and assign the next company to the children of the current node. 
# We will continue this until we have assigned all the companies. 
# After we have assigned all the companies, we will count the number of bad nodes.
# Complexity: O(n)

from sys import stdin

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.parent = None
        self.company = 0
        self.bad = False

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def assign_company(self, company):
        self.company = company
        for child in self.children:
            child.assign_company(company)

    def get_num_children(self):
        if not self.children:
            return 0
        return 1 + sum([child.get_num_children() for child in self.children])

    def get_num_bad_nodes(self):
        if not self.children:
            return 0
        if self.bad:
            return 1 + sum([child.get_num_bad_nodes() for child in self.children])
        return sum([child.get_num_bad_nodes() for child in self.children])

    def __str__(self):
        return "{} -> {}".format(self.key, [child.key for child in self.children])


def dfs(root, company):
    # assign company to children
    root.assign_company(company)
    # assign company to children of children
    for child in root.children:
        dfs(child, company + 1)


def get_num_companies(root):
    return max(root.company, 1)


def get_num_bad_nodes(root):
    return root.get_num_bad_nodes()


def main():
    n, k = [int(x) for x in stdin.readline().split()]
    nodes = [Node(i) for i in range(1, n + 1)]
    for _ in range(n - 1):
        x, y = [int(x) for x in stdin.readline().split()]
        nodes[x - 1].add_child(nodes[y - 1])
        nodes[y - 1].add_child(nodes[x - 1])
    root = nodes[0]
    root.bad = True
    dfs(root, 1)
    num_companies = get_num_companies(root)
    num_bad_nodes = get_num_bad_nodes(root)
    if num_bad_nodes > k:
        print(-1)
    else:
        print(num_companies)
        print(" ".join([str(node.company) for node in nodes]))


if __name__ == "__main__":
    main()