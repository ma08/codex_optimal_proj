
def main():
    n = int(input())
    s = input()
    max_count = 0
    max_str = ""
    for i in range(n-1):
        current_str = s[i:i+2]
        current_count = s.count(current_str)
        if current_count > max_count:
            max_count = current_count
            max_str = current_str
    print(max_str)

if __name__ == "__main__":
    main()