import math

def round_dances(dancers):
    return math.factorial(dancers) // (2 * math.factorial(dancers // 2))

if __name__ == '__main__':
    dancers = int(input())
    print(round_dances(dancers))
