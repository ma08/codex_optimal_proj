
import heapq

def main():
    n = int(input())
    ingredients = [int(x) for x in input().split()]  # list of ingredients
    heapq.heapify(ingredients)  # heapify the ingredients
    while len(ingredients) > 1:  # while there are more than 1 ingredients left
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2)  # add the average of the two smallest ingredients to the heap
    print(ingredients[0])  # print the last ingredient

if __name__ == '__main__':
    main()
