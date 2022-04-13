

def main():
    """
    Main method to be called at runtime.
    """
    contest_info = input().split(" ")
    num_contestants = int(contest_info[0])
    num_problems = int(contest_info[1])
    carrots = 0 # number of carrots eaten
    for i in range(0, num_contestants):
        contestant = input()
        if "carrot" in contestant.lower():
            carrots += 1 # increment if contestant ate carrot
    print(carrots)

if __name__ == "__main__":
    main()
