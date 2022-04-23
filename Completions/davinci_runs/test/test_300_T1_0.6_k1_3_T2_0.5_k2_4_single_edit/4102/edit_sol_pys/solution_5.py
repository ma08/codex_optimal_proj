

def is_lucky(n):
    n = list(map(int, str(n)))
    if len(n) % 2 == 0:
        first_half = sum(n[:len(n)//2])
        second_half = sum(n[len(n)//2:])
        if first_half == second_half:
            return "Yes"
        else:
            return "No"
    return "No"

# if __name__ == '__main__':
#     n = sys.stdin.read().strip()
#     print(is_lucky(n))
