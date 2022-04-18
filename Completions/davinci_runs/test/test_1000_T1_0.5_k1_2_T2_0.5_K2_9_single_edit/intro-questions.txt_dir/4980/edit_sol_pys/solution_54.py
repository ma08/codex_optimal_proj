
def check_if_pink(string, list):
    return any(word in string.lower() for word in list)

def main():
    total = int(input())
    list = ["pink", "rose"]
    count = 0
    for i in range(total):
        string = input()
        if check_if_pink(string, list):
            count += 1
    if count > 0:
        print(count)
    else:
        print("I must watch Star Wars with my daughter")

main()
