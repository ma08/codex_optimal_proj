class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


def main():
    string = input()
    stack = Stack()
    for c in string:
        if c == '<':
            stack.pop()
        else:
            stack.push(c)
    print(stack)


main()
