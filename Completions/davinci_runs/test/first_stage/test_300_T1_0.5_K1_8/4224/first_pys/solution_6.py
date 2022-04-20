

# N = int(input())
# a = list(map(int, input().split()))

N = 3
a = [5, 2, 4]

def divide(x):
    return x // 2

def multiply(x):
    return x * 3

def count_even(a):
    return len([x for x in a if x % 2 == 0])

def count_odd(a):
    return len([x for x in a if x % 2 != 0])

def count_three(a):
    return len([x for x in a if x % 3 == 0])

def main():
    print('count_even:', count_even(a))
    print('count_odd:', count_odd(a))
    print('count_three:', count_three(a))
    if count_even(a) == N:
        print(N//2)
    else:
        if count_three(a) > count_odd(a):
            print(count_three(a) + (N - count_three(a))//2)
        else:
            print(count_odd(a))

if __name__ == '__main__':
    main()