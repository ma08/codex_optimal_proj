
n = int(input())
s = input()

def get_num_sequences(n, s):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num_sequences = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if len(substring) % 2 == 0:
                    num_sequences += get_num_sequences(len(substring), substring)
        return num_sequences

num_sequences = get_num_sequences(n, s)
print(num_sequences % 1000000007)
