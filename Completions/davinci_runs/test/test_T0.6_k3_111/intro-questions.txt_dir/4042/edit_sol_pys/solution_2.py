

def main():
    x = float(input())
    a = int(x)  # дорівнює цілій частині
    b = round((x - int(x)) * 100)  # дорівнює дробовій частині
    print(a, b)  # виводить на екран

main()
