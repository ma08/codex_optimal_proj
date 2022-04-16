

def main():
    w = input()
    print("Yes") if (w.count("a") % 2 == 0 and w.count("b") % 2 == 0 and w.count("c") % 2 == 0) else print("No")

if __name__ == '__main__':
    main()
