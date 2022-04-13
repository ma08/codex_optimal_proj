

def main():
    left, right = map(int, input().split())
    if left == right:
        print("Even %d" % (left + right))
    elif left > right:
        print("Odd %d" % (2 * left))
    else: 
        print("Odd %d" % (2 * right))

if __name__ == "__main__":
    main()
