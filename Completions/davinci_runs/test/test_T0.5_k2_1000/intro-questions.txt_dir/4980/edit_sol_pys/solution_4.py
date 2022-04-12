

def check_if_pink(string, color):
    return color in string.lower() or color in string.lower()

def main():
    total = int(input())
    count = 0
    for i in range(total):
        string = input()
        if check_if_pink(string, "pink") or check_if_pink(string, "rose") or check_if_pink(string, "rose"):
            count += 1
    if count > 0:
        print(count)
    else:
        print("I must watch Star Wars with my daughter")

main()
