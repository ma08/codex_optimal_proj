
import heapq

def main():
    n = int(input())
    ingredients = [int(x) for x in input().split()]  # list of ingredients
    heapq.heapify(ingredients)  # heapify the list
    while len(ingredients) > 1:  # while there are more than 1 ingredient
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2)  # add the average of the first 2 ingredients
    print(ingredients[0])  # print the average of the ingredients

if __name__ == '__main__':
    main()
