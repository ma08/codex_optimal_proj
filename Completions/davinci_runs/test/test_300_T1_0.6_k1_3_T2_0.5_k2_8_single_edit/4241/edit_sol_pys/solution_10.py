

s = input("Enter string: ")
t = input("Enter substring: ")

def main(s, t):
    count = 0

    for i in range(len(s)):
        if s[i:i+len(t)] == t: #s[i:i+len(t)] is a slice of s from i to i + len(t)
            return count
        else:
            count += 1

print(main(s, t))
