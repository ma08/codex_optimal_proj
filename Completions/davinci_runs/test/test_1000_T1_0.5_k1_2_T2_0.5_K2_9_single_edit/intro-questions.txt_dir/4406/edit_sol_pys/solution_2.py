

def main():
    n, k = [int(x) for x in input().split()]
    messages = [int(x) for x in input().split()]
    messages.reverse()
    conversations = [0] * k
    for message in messages:
        if message not in conversations[1:]:
            conversations.pop()
            conversations.insert(0, message) 
    print(len(conversations) - conversations.count(0))
    print(' '.join([str(x) for x in conversations]))

main()
