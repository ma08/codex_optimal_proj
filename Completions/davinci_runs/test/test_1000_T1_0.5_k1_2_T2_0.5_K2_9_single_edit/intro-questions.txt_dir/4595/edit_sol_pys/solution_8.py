
def main():
    """
    1. get the string s
    2. find the index of 'A' and 'Z'
    3. compute the distance
    """
    s = input()
    index_A = s.find('A')
    index_Z = s.rfind('Z')
    print(index_Z - index_A + 1)

if __name__ == '__main__':
    main()
