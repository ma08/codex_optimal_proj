
def main():
    """
    1. get the string s
    2. find the index of 'A' and 'Z'
    3. compute the distance
    """
    s = input()
    idx_a = s.find('A')
    idx_z = s.rfind('Z')
    print(idx_z - idx_a + 1)

if __name__ == '__main__':
    main()
