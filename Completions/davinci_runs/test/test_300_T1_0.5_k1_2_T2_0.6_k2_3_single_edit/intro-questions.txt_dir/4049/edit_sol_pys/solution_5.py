

def main():
    # get input
    n = int(input())
    a = input().split()
    b = input().split()
    
    # get counts
    a_count = [0] * 3
    b_count = [0] * 3
    for i in range(n):
        if a[i] == b[i]:
            continue
        elif (a[i] + 1) % 3 == b[i]:
            a_count[b[i]] += 1
            b_count[(b[i] + 1) % 3] += 1
        else:
            a_count[b[i]] += 1
            b_count[(b[i] - 1) % 3] += 1
    
    # get winner
    if a_count[0] > b_count[0]:
        print("Anton")
    elif a_count[0] < b_count[0]:
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    main()
