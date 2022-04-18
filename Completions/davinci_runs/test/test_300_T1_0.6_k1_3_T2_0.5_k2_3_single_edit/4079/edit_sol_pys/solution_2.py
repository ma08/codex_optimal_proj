

def diverse_string(string):
    if len(set(string)) == len(string):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        print(diverse_string(string))
