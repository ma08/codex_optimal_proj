

def solution(n, k, id_list):
    conversations = [id_list[0]]
    for id in id_list[1:]:
        if id not in conversations: 
            if len(conversations) == k:
                conversations.pop(0)
            conversations.append(id)
    return len(conversations)

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
