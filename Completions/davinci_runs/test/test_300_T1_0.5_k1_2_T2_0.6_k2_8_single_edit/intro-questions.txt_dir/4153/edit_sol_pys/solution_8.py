
S = raw_input()

zeroes = S.count("0")
zeroes_at_beginning_or_end = len(S) - len(S.lstrip("0").rstrip("0"))

print(zeroes - zeroes_at_beginning_or_end)
