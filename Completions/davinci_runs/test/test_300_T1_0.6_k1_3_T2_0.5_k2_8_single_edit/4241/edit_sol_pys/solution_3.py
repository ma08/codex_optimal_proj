

def main():
    count = 0

    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            return count
        else:
            count += 1

print(main())
