

def solution(n, k, id_list):
    conversations = set()
    for i in range(n):
        id = id_list[i]
        if id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations.add(id)
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
