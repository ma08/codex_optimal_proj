

def solution(n, k, id_list, m):
    conversation = []
    for id in id_list:
        if id not in conversation:
            if len(conversation) >= k:
                conversation.pop()
            conversation = [id] + conversation
    m = len(conversation)
    return conversation

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    id_list = list(map(int, input().split()))
    m = 0
    conversation = solution(n, k, id_list, m)
    print(m)
    print(*conversation)
