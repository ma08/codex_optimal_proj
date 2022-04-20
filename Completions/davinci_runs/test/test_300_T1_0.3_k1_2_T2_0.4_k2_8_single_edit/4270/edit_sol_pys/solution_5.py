

import heapq

def main():
    n = int(input())
    ingredients = [int(x) for x in input().split()] # [1, 2, 3, 4, 5]
    heapq.heapify(ingredients) # [1, 2, 3, 4, 5]
    while len(ingredients) > 1: # 5 > 1
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2) # [1, 2, 3, 4, 5] -> [1.5, 2, 3, 4, 5] -> [2, 2, 3, 4, 5] -> [2.5, 3, 3, 4, 5] -> [3, 3, 3, 4, 5] -> [3.5, 3, 4, 4, 5] -> [4, 3, 4, 4, 5] -> [4.5, 4, 4, 4, 5] -> [4, 4, 4, 4, 5] -> [4.5, 4, 4, 5, 5] -> [4, 4, 4, 5, 5] -> [4.5, 4, 5, 5, 5] -> [4, 4, 5, 5, 5] -> [4.5, 5, 5, 5, 5] -> [5, 5, 5, 5, 5] -> [5, 5, 5, 5]
    print(ingredients[0]) # 5

if __name__ == '__main__':
    main()
