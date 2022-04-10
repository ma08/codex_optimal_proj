
def process(n, k, x, a_list, b_list):
    if x < n - k + 1:
        return -1
    else:

        return sum(a_list) + sum(b_list)

def main():
    n, k, x = [int(x) for x in input().strip().split()]
    a_list = [int(x) for x in input().strip().split()]
    b_list = [int(x) for x in input().strip().split()]
    result = process(n, k, x, a_list, b_list)
    print(result)

if __name__ == "__main__":
    main()
