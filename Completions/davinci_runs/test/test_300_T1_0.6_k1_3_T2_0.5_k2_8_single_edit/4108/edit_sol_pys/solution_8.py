

def can_make_equal(S, T):
    if sorted(S) != sorted(T):
        return False
    return True

if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if can_make_equal(S, T) else "No")
