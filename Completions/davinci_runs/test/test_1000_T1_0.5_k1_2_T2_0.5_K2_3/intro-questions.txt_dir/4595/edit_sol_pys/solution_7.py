
def main():
    """
    1. get the string S
    2. find the index of 'A' and 'Z'
    3. compute the distance
    """
    S = input()
    idx_A = S.find('A')
    idx_Z = S.rfind('Z')
    print(idx_Z - idx_A + 1)

if __name__ == '__main__':
    main()
