

def main():
    nums = [int(x) for x in input().split()]
    stacks = [Stack() for x in range(len(nums))]
    for i in range(len(nums)):
        stacks[i].push(nums[i])
    for i in range(len(nums)):
        if stacks[i].size() >= 2:
            if stacks[i].top() > stacks[i+1].top() + 1:
                print("NO")
                return
            elif stacks[i].top() == stacks[i+1].top() + 1:
                stacks[i+1].push(stacks[i].pop())
    print("YES")

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

main()