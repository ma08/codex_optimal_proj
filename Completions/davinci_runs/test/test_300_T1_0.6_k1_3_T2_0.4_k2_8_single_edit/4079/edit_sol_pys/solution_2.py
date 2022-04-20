

def diverse_string(string):
    if len(set(string)) == len(string) and len(string) == ord(string[-1]) - ord(string[0]) + 1 and len(string) <= 26:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        print(diverse_string(string))
