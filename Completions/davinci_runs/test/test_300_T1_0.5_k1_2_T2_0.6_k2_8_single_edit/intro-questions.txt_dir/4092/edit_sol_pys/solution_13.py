
def main():  
    from collections import deque
    q = deque([1, 2, 3])
    q.append(4)
    print(q)
    q.appendleft(5)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)
    if __name__ == '__main__':
        main()
