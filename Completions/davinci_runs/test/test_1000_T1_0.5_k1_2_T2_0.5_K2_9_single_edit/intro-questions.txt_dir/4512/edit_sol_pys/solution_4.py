

def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = input()
        if query[0] == "1":
            s = s[:int(query[2])-1] + query[4] + s[int(query[2]):]
        elif query[0] == "2":
            print(len(set(s[int(query[2])-1:int(query[4])]))

if __name__ == "__main__":
    main()
