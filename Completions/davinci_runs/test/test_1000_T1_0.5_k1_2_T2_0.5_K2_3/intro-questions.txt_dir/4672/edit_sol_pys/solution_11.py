# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def get_mean(arr):
    return sum(arr) / len(arr)
    
def get_std(arr):
    mean = get_mean(arr)
    squared_diff = [(x - mean) ** 2 for x in arr]
    mean_of_squared_diff = get_mean(squared_diff)
    return math.sqrt(mean_of_squared_diff)
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(get_mean(arr))
    print(get_std(arr))
