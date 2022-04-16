

def main():
    n, k = [int(x) for x in input().split()]  # n is the number of messages, k is the number of conversations
    messages = [int(x) for x in input().split()]
    messages.reverse()  # reverse the messages so that the most recent message is at the end of the list
    conversations = []  # list that will hold the conversations
    for message in messages:
        if message not in conversations:  # check if the message is not already in the conversations list
            if len(conversations) == k:  # check if the conversations list is full
                conversations.pop()  # remove the oldest conversation
            conversations.insert(0, message)  # insert the message at the front of the conversations list
    print(len(conversations))  # print the number of conversations
    print(' '.join([str(x) for x in conversations]))  # print the conversations

main()
