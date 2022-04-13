

def check_harashad():
    n = int(input())
    s_sum = sum([int(x) for x in str(n)])
    return "Yes" if n % s_sum == 0 else "No"

if __name__ == '__main__':
    print(check_harashad())
