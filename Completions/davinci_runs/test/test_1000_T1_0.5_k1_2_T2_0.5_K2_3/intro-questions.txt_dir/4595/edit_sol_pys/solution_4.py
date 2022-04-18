
def main():
    s = input()
    idx_A = s.find('A')
    idx_Z = s.rfind('Z')
    print(idx_Z - idx_A + 1)

if __name__ == '__main__':
    main()
