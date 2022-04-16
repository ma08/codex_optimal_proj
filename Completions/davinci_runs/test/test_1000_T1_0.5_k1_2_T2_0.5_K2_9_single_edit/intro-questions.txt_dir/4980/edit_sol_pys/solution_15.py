

def check_if_pink(string):
    return string.lower() == "pink" or string.lower() == "rose"

def main():
    total = int(input())
    count = 0
    for i in range(total):
        string = input()
        if check_if_pink(string):
            count += 1
    if count > 0:
        print(count)
    else:
        print("I must watch Star Wars with my daughter")

main()
