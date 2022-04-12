

def main():
    # parse input
    max_diff = int(input())
    queue = input().strip()
    # count the number of men and women in the queue
    men = queue.count('M') - 1
    women = queue.count('W') - 1
    # print the minimum of the number of men and women in the queue
    # since that's the maximum number of people that can be let in
    # without exceeding the maximum difference of men and women
    print(min(men, women))

if __name__ == "__main__":
    main()
