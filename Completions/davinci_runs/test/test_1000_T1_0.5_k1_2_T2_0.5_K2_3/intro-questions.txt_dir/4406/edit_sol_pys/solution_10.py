

def main():
    n, k = [int(x) for x in input().split()]
    messages = [int(x) for x in input().split()][::-1]
    conversation = []
    for message in messages:
        if message not in conversation:
            if len(conversation) == k:
                conversation.pop()
            conversation.insert(0, message)
    print(len(conversation))
    print(' '.join([str(x) for x in conversation]))

main()
