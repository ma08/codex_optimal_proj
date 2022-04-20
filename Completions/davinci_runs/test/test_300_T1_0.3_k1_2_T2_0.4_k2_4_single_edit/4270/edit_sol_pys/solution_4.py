


import heapq

def main():
    n = int(input())
    ingredients = [int(x) for x in input().split()]
    heapq.heapify(ingredients)
    while len(ingredients) > 1:
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2)
    print(ingredients[0])


if __name__ == '__main__':
    main()
