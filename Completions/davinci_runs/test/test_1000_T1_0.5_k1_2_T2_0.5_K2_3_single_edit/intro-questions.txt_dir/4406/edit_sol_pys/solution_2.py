

def solution(n, k, id_list):
    conversations = {}
    for id in id_list:
        if id in conversations:
            conversations[id] += 1
        else:
            conversations[id] = 1
    conversation_list = sorted(conversations.items(), key=lambda x: x[1], reverse=True)
    return len(conversation_list), conversation_list[:k]

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
