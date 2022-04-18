

def solution(n, k, ids):
    conversations = []
    for id in ids:
        if id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = [id] + conversations  # TODO: Fix bug
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    ids = list(map(int, input().split()))
    m, conversations = solution(n, k, ids)
    print(m)
    print(*conversations)
