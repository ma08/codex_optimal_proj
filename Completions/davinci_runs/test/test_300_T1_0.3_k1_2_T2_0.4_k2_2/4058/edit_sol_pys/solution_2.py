


#-----Solution------

n, m = map(int, input().split())
a = list(map(int, input().split())) 
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# We can use the same approach as in the previous problem
# to find the number of needed heaters

# The answer is the sum of the number of needed heaters
# for the first and the second list

print(min(n, m))
