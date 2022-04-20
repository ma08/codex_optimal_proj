
def can_make_equal(S, T):
    return len(S) == len(T) and sorted(S) == sorted(T)

if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if can_make_equal(S, T) else "No")
