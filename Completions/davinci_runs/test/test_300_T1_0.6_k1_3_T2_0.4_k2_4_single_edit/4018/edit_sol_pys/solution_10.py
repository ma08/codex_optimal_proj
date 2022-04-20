

def main():
    # read in the number of characters in string and the number of subsequences to generate
    n, k = [int(x) for x in input().split()]
    # read in the string
    s = input()
    # set the initial cost to 0
    cost = 0
    # set the number of subsequences generated to 1, since the total string is a subsequence
    sub_num = 1
    # loop through the string
    for i in s:
        # if the number of subsequences generated is greater than k, then it is impossible to generate k unique subsequences
        if sub_num > k:
            return -1
        # if the number of subsequences generated is less than k, then add the number of deleted characters to the cost
        # the number of deleted characters is equal to the number of characters in the string minus the number of subsequences generated
        else:
            cost += n - sub_num
            # increment the number of subsequences by 1
            sub_num += 1
    # if the number of subsequences generated is equal to k, then we have generated k unique subsequences
    elif sub_num == k:
        return cost
    # if the number of subsequences generated is less than k and we have not reached the end of the string, then it is impossible to generate k unique subsequences
    elif sub_num < k:
        return -1

if __name__ == "__main__":
    print(main())
