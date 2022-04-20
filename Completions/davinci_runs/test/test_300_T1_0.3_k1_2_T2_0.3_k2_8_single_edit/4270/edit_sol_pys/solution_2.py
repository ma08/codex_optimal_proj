
import heapq

def main():
    n = int(input())  # number of ingredients
    ingredients = [int(x) for x in input().split()]  # list of ingredients
    heapq.heapify(ingredients)  # heapify the ingredients
    while len(ingredients) > 1:  # while there is more than one ingredient
        heapq.heappush(ingredients, (heapq.heappop(ingredients) + heapq.heappop(ingredients)) / 2)  # push the average of the two smallest ingredients
    print(ingredients[0])  # print the final ingredient

if __name__ == '__main__':
    main()
