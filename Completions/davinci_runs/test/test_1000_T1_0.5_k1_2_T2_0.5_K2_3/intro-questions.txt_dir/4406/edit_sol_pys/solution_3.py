

def solution(n, k, conversations):
    conversations = []
    for id in conversations:
        if id not in conversations:
            if len(conversations) >= k:
                conversations.pop()
            conversations = [id] + conversations
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    ids = list(map(int, input().split()))
    m, conversations = solution(n, k, conversations)
    print(m)
    print(*conversations)
