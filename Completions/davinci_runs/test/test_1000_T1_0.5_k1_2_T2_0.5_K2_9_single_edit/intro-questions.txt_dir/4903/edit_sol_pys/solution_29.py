

def main():
    n = int(input())
    for i in range(n):
        jon = input().strip()
        doc = input().strip()
        if len(jon)>=len(doc):
            print("go")
        else:
            print("no")

main()
