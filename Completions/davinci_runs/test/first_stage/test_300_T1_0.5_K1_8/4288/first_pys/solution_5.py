

def is_poor(A, B, C):
    return (A == B and A != C) or (B == C and B != A) or (C == A and C != B)

def main():
    A, B, C = map(int, input().split())
    if is_poor(A, B, C):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()