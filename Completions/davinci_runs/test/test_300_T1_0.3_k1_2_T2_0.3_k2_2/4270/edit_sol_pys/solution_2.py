

import heapq

def main():
    n = int(input())
    ingredients = [int(x) for x in input().split()] # ingredients = [1, 2, 3, 4, 5]
    heapq.heapify(ingredients) # ingredients = [1, 2, 3, 4, 5]
    while len(ingredients) > 1: # len(ingredients) = 5
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2) # ingredients = [1.5, 2.5, 3, 4, 5]
    print(ingredients[0]) # 1.5

if __name__ == '__main__':
    main()
