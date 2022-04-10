def solve(n):
  if n <= 26:
    return chr(n + 96)
  else:
    word_len = 1
    while True:
      if n - 26**word_len <= 0:
        break
      n -= 26**word_len
      word_len += 1
    n -= 1
    answer = ''
    for _ in range(word_len):
      answer = chr(n % 26 + 97) + answer
      n = n // 26
    return answer

print(solve(N))
