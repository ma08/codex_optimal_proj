

def is_sorted(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            return False
    return True


if is_sorted(sequence):
    print("YES")
else:
    print("NO")
