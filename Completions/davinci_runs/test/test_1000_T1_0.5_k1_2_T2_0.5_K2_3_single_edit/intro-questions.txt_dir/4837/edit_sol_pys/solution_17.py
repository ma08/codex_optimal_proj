
import sys  # this is used to take input from the console

def main():
    r = int(sys.stdin.readline().strip())  # the number of rounds
    sven = sys.stdin.readline().strip()  # sven's moves
    n = int(sys.stdin.readline().strip())  # the number of friends
    friends = []  # list to hold friend moves
    for i in range(n):  # loop to add friend moves to list
        friends.append(sys.stdin.readline().strip())  # add friend moves to list

    score = 0  # score variable
    for i in range(r):  # loop to iterate through rounds
        for friend in friends:  # loop to iterate through friends
            if sven[i] == 'R':  # if sven uses rock
                if friend[i] == 'S':  # and friend uses scissors
                    score += 2  # increment score by 2
                elif friend[i] == 'P':  # else if friend uses paper
                    score += 1  # increment score by 1
            elif sven[i] == 'S':  # else if sven uses scissors
                if friend[i] == 'P':  # and friend uses paper
                    score += 2  # increment score by 2
                elif friend[i] == 'R':  # else if friend uses rock
                    score += 1  # increment score by 1
            elif sven[i] == 'P':  # else if sven uses paper
                if friend[i] == 'R':  # and friend uses rock
                    score += 2  # increment score by 2
                elif friend[i] == 'S':  # else if friend uses scissors
                    score += 1  # increment score by 1
    print(score)

    score = 0  # score variable
    for i in range(r):  # loop to iterate through rounds
        for friend in friends:  # loop to iterate through friends
            if sven[i] == 'R':  # if sven uses rock
                if friend[i] == 'S':  # and friend uses scissors
                    score += 2  # increment score by 2
            elif sven[i] == 'S':  # else if sven uses scissors
                if friend[i] == 'P':  # and friend uses paper
                    score += 2  # increment score by 2
            elif sven[i] == 'P':  # else if sven uses paper
                if friend[i] == 'R':  # and friend uses rock
                    score += 2  # increment score by 2
    score += r  # increment score by r
    print(score)

if __name__ == "__main__":  # run main function
    main()
