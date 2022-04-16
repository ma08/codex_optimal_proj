

def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = input()
        if query[0] == "1":
            s = s[:int(query[2])-1] + query[4] + s[int(query[2]):] # query[2] is the index of the char to be changed
        elif query[0] == "2":
            print(len(set(s[int(query[2])-1:int(query[4])]))) # query[2] is the start index of the substring and query[4] is the end index

if __name__ == "__main__":
    main()
