

def main():
    # parse input
    max_diff = int(input())
    queue = input()
    # count the number of men and women in the queue
    men = queue.count('M')
    women = queue.count('W')
    # print the minimum of the number of men and women in the queue
    # since that's the minimum number of people that can be let in
    # without exceeding the maximum difference
    print(min(men, women))

if __name__ == "__main__":
    main()
