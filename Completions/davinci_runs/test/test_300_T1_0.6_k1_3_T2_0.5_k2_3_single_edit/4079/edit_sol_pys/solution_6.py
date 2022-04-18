

def diverse_string(string):
    if len(set(string)) == len(string) and len(string) == ord(string[-1]) - ord(string[0]) + 1:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    for i in range(int(input())):
        string = input()
        print(diverse_string(string))
