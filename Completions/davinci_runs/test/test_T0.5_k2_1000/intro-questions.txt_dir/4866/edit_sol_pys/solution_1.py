

def main():
    month, date = input().split()
    if month in ["OCT", "DEC"] and date == "25":
        print("yup")
    else:
        print("nope")

if __name__ == "__main__":
    main()
