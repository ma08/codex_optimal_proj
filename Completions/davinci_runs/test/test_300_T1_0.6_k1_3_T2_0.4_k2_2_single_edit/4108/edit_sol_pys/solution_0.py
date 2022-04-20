
def can_make_equal(S, T):
    if len(S) != len(T):  # check if the length is equal
        return False
    if sorted(S) != sorted(T):  # check if the characters are equal
        return False
    return True

if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if can_make_equal(S, T) else "No")
