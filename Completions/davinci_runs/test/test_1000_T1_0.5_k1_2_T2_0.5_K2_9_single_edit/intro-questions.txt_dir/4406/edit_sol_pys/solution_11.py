

def solution(n, k, id_list):
    conversations = set()
    for id in id_list:
        if len(conversations) < k:
            conversations.add(id)
        elif id not in conversations:
            conversations.pop()
            conversations.add(id)
    return len(conversations), sorted(list(conversations))

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
