

def main():
    n, k = [int(x) for x in input().split()]
    messages = [int(x) for x in input().split()]
    messages.reverse()
    conversations = []
    while messages:
        message = messages.pop()
        if message not in conversations and len(conversations) < k:
            conversations.insert(0, message)
    print(len(conversations))
    print(' '.join([str(x) for x in conversations]))

main()
