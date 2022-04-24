
def main():
    s = input()
    t = input()

    print(sum(1 if s != t else 0 for s, t in zip(s, t)))

if __name__ == '__main__':
    main()
