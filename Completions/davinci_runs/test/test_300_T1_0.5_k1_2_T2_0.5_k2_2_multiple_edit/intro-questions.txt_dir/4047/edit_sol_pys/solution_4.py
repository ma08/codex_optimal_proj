

n = int(input())  # input the number of elements of the array
x = list(map(int, input().split()))  # input the elements of the array

x.sort()  # sort the elements of the array


min_cost = float('inf')  # set the minimum cost to infinity
for i in range(n):
    cost = 0  # cost is 0 at the beginning, it is used to calculate the cost
    for j in range(n):
        cost += abs(x[j] - x[i])  # calculate the cost
    min_cost = min(min_cost, cost)  # set the minimum cost


print(min_cost)  # print the minimum cost
