

if __name__ == '__main__':
    S = input() 
    print("Yes" if len(S) == len(set(S)) else "No")
