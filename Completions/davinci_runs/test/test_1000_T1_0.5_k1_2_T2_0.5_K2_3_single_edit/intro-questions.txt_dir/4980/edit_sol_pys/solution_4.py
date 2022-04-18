

def checkIfPink(string):
    return "pink" in string.lower() or "rose" in string.lower()

def main():
    total = int(input())
    count = 0
    for i in range(total):
        string = input()
        if checkIfPink(string):
            count += 1
    if count > 0:
        print(count)
    else:
        print("I must watch Star Wars with my daughter")

main()
