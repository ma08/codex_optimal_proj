
def main(s):
    return s[-1] if s[-1] == "T" else "T"

if __name__ == "__main__":
    s = input()
    print(main(s))
