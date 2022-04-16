

def solution(n, k, id_list):
    conversations = list(range(k))
    for id in id_list:
        if id not in conversations[1:]:
            conversations.pop()
            conversations = [id] + conversations[1:]
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
