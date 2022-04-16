
def main():
    """
    1. get the string s
    2. find the index of 'A' and 'Z'
    3. compute the distance
    """
    s = input()
    idx_A = s.find('A')
    idx_Z = s.rfind('Z')
    print(idx_Z - idx_A + 1)

if __name__ == '__main__':
    main()
