

def solution(n, k, id_list):
    conversations = []
    for id in id_list:
        if id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = [id] + conversations
    return conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    conversations = solution(n, k, id_list)
    print(len(conversations))
    print(*conversations)
