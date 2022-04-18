

def main():
    a = int(input("a = "))
    b = int(input("b = "))

    c = [1,2,3]
    c.remove(a)
    c.remove(b)
    print(c[0])

if __name__ == "__main__":
    main()
