

def immigration(num_list):
    for i in num_list:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            return "DENIED"
    return "APPROVED"

def main():
    n = int(input())
    num_list = [int(i) for i in input().split()]
    print(immigration(num_list))

if __name__ == '__main__':
    main()