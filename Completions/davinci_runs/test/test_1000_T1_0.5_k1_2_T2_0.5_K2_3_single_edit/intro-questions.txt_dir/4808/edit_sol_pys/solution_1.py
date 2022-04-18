

    # input
def main():
    n, d_m = map(int, input().split())
    d_n = list(map(int, input().split()))
    # count the number of years that the snow came in the same day
    d_n.append(d_m)
    count = 0
    for i in range(n-1, -1, -1):
        if d_n[i] > d_n[i+1]:
            count += 1
        else:
    # output
            break
    print("It hadn't snowed this early in " + str(count) + " years!")

if __name__ == "__main__":
    main()
