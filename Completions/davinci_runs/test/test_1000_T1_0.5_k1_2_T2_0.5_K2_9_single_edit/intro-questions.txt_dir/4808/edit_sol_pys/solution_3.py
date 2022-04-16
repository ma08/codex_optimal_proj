

def main():
    n, d_m = map(int, input().split())
    d_n = list(map(int, input().split()))
    d_n.append(d_m)
    count = 0
    for i in range(n-1, -1, -1):  # range(start, stop, step)
        if d_n[i] > d_n[i+1]:
            count += 1
        else:
            break
    print("It hadn't snowed this early in " + str(count) + " years!")

if __name__ == "__main__":
    main()
