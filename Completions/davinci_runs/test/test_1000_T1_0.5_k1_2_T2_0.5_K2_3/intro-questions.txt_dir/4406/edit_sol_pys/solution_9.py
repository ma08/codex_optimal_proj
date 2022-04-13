

def solution(n, k, id_list):
    conversations = []
    for ids in id_list:
        if ids not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = [ids] + conversations
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m, conversations = solution(n, k, id_list)
    print(m)
    print(*conversations)
