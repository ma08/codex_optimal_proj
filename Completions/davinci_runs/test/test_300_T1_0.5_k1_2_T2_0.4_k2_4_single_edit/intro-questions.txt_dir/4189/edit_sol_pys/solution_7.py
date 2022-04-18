


def cheese_sort(cheese):
    return cheese[1]

def main():
    n = int(input())
    cheese_list = []
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        cheese_list.append(cheese)
    cheese_list.sort(key=cheese_sort)
    for cheese in cheese_list:
        print(cheese[0])

if __name__ == "__main__":
    main()
