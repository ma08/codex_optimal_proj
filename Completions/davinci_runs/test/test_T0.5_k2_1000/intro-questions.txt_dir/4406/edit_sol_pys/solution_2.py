

def solution(n, k, ids):
    conversations = []
    for _id in ids:
        if _id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = [_id] + conversations
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    ids = list(map(int, input().split()))
    m, conversations = solution(n, k, ids)
    print(m)
    print(*conversations)
