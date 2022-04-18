

def is_valid(c, l, h):
    if c < l or c > h:
        return False
    if len(set(str(c))) != 6:
        return False
    if any(c % int(d) != 0 for d in str(c)):
        return False
    return True

def num_valid(l, h):
    return sum(1 for c in range(l, h+1) if is_valid(c, l, h))

def main():
    l, h = map(int, input().split())
    print(num_valid(l, h))

if __name__ == "__main__":
    main()
