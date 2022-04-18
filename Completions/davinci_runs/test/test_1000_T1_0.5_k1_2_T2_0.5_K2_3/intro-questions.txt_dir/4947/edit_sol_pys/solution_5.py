

def main():
    x = float(input())
    print(int(round(1000 * (5280/4854) * x)))  # 5280 feet in a mile and 4854 meters in a mile

main()
