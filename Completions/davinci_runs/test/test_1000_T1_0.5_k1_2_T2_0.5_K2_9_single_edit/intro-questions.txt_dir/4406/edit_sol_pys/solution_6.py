

def main():
    n, k = [int(x) for x in raw_input().split()]
    messages = [int(x) for x in raw_input().split()]
    messages.reverse()
    conversations = []
    for message in messages:
        if message not in conversations:
            if len(conversations) == k:
                conversations.pop()
            conversations.insert(0, message)
    print(len(conversations))
    print(' '.join([str(x) for x in conversations]))

main()
