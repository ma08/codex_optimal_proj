

def can_make_equal(s, t):
    if len(s) != len(t):
        return False
    if sorted(s) != sorted(t):
        return False
    return True

if __name__ == "__main__":
    s = input()
    t = input()
    print("Yes" if can_make_equal(s, t) else "No")
