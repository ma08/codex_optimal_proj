import string

N = int(input()) + 1

def solve(N):
  if N <= 26:
    return string.ascii_uppercase[N - 1]
  else:
    word_len = 1
    while True:
      if N - 26**word_len <= 0:
        break
      N -= 26**word_len
      word_len += 1
    N -= 1
    alphabet = string.ascii_uppercase
    answer = ''
    for _ in range(word_len):
      answer = alphabet[N % 26] + answer
      N = N // 26
    return answer

print(solve(N))
