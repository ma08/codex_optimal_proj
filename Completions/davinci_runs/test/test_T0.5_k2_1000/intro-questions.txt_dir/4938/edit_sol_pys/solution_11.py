

def main():
    # parse input 
    max_diff = int(input())
    queue = input()
    # count the number of boys and girls in the queue
    boys = queue.count('B')
    girls = queue.count('G')
    # print the minimum of the number of boys and girls in the queue
    # since that's the maximum number of people that can be let in without
    # exceeding the maximum difference
    print(min(boys, girls))

if __name__ == "__main__":
    main()
