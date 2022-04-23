S = raw_input()

zeros = S.count("0")
zeros_at_beginning_and_end = len(S) - len(S.lstrip("0").rstrip("0"))
print zeros - zeros_at_beginning_and_end
