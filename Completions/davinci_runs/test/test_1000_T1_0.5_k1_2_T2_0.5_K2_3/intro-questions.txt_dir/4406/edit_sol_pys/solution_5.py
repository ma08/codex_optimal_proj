# https://codeforces.com/problemset/problem/1145/A

def main():
    n, k = [int(x) for x in input().split()]
    messages = [int(x) for x in input().split()]
    messages.reverse()
    conversation = []
    for message in messages:
        if message not in conversation:
            if len(conversation) == k:
                conversation.pop()
            conversation.insert(0, message)
    print(len(conversation))
    print(' '.join([str(x) for x in conversation]))


if __name__ == '__main__':
    main()
