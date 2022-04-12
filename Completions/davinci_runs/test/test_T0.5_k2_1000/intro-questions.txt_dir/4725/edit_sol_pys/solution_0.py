
def main(inp):
    if len(inp) <= 2: return 0
    freq = {}
    for char in inp: freq[char] = freq.get(char, 0) + 1
    if len(freq) <= 2: return 0
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    if freq[2][1] == 1: return len(inp) - 2
    else: return len(inp) - 1 - freq[1][1] - freq[2][1]
