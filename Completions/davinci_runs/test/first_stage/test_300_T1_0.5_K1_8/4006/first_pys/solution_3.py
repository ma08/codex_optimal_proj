

def main():
    """main"""
    num = int(input())
    print(count(num))

def count(num):
    """count"""
    if num < 10:
        return num
    else:
        return count(num//10) + count(num//10 - 1)

main()