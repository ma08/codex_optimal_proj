import sys

s = input()
t = input()

def main(s, t):
    count = 0

    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            print(count)
            sys.exit()
        else:
            count += 1
    print(-1)
main(s, t)
