

def main():
    """
    Main method to be called at runtime.
    """
    contest_info = input().split(" ")
    num_contestants = int(contest_info[0])
    num_problems = int(contest_info[1])
    carrots = 1
    for i in range(0, num_contestants):
        contestant = input()
        carrots *= int(contestant)
    print(carrots)

if __name__ == "__main__":
    main()
