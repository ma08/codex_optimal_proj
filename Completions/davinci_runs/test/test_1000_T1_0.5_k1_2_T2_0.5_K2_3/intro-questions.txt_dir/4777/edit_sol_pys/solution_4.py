

def max_sequence(seq):
    for i in range(1, len(seq)):
        if not seq[i - 1] < seq[i]:
            return False
    return True


print(max_sequence([1, 2, 3, 4, 5, 6]))
