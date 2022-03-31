

def get_num_sequences(s):
    num_sequences = 1
    num_open_brackets = 0
    for char in s:
        if char == '(':
            num_open_brackets += 1
        elif char == ')':
            num_sequences *= num_open_brackets
        else:
            raise Exception('Error: invalid character')
    return num_sequences

def get_num_sequences_with_substrings(s):
    num_sequences = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) % 2 == 0:
                num_sequences += get_num_sequences(substring)
    return num_sequences

if __name__ == '__main__':
    n = int(input())
    s = input()
    num_sequences = get_num_sequences_with_substrings(s)
    print(num_sequences % 1000000007)
