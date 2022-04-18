

def main():
    n, k = [int(x) for x in input().split()] # n = number of messages, k = number of conversations
    messages = [int(x) for x in input().split()] # messages = list of messages
    messages.reverse() # reverse the list to make it easier to pop from the end
    conversations = [] # list to store the conversations
    for message in messages: # loop through all the messages
        if message not in conversations: # if the message is not in the conversations list
            if len(conversations) == k: # if the conversations list is full
                conversations.pop() # pop the last element (the oldest conversation)
            conversations.insert(0, message) # insert the new conversation at the beginning of the list
    print(len(conversations)) # print the number of conversations
    print(' '.join([str(x) for x in conversations])) # print the conversations

main()
