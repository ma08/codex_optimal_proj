
def can_make_equal(S, T):
    if len(S) < len(T):
        return False
    return all(S.count(char) >= T.count(char) for char in set(T))

if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if can_make_equal(S, T) else "No")
