

def can_make_equal(S, T):
    if len(S) != len(T):
        return False
    if sorted(S) != sorted(T):
        return False
    return True

if __name__ == "__main__":
    S = input().strip()
    T = input().strip()
    print("Yes" if can_make_equal(S, T) else "No")
