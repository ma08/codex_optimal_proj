

def solution(n, k, id_list):
    conversations = []
    for id in id_list:
        if id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = conversations + [id]
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
