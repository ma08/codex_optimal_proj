

input_s = input()
input_t = input()

def main(input_s, input_t):
    count = 0

    for i in range(len(input_s)):
        if input_s[i:i+len(input_t)] == input_t:
            return count
        else:
            count += 1

print(main(input_s, input_t))
