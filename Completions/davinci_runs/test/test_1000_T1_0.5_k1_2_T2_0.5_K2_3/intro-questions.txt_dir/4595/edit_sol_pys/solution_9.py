

def main():
    """
    1. get the string s
    2. find the index of 'A' and 'Z' (or 'a' and 'z')
    3. compute the distance
    """
    s = input()
    idx_A = s.find('A')  # or min(s.find('A'), s.find('a'))
    idx_Z = s.rfind('Z')  # or max(s.rfind('Z'), s.rfind('z'))

    print(idx_Z - idx_A + 1)

if __name__ == '__main__':
    main()
