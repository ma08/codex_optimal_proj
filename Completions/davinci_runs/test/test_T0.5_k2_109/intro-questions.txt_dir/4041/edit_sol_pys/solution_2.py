

def get_max_substring(s, t):
    count = len(t)
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            count = 0
            break
        else:
            count = min(count, len(t) - len(set(s[i:i + len(t)]) & set(t)))
    return count

if __name__ == "__main__":
    print(get_max_substring(input(), input()))
