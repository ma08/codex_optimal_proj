

n = int(input())
s = input()

two_grams = [s[i:i+2] for i in range(len(s)-1)]

print(max(set(two_grams), key=two_grams.count))