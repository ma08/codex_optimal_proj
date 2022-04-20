

def can_make_equal(S, T):
    if len(S) != len(T):
        return False
    S = sorted(S)
    T = sorted(T)
    return True

if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if can_make_equal(S, T) else "No")
