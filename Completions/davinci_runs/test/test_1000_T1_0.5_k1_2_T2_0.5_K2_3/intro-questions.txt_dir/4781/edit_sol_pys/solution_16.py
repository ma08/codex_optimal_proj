

# k = int(input())
# n = int(input())

# for i in range(n):
#     t, z = input().split() 
#     t = int(t)
#     if (t + k) % 8 == 0:
#         k = 8
#     else:
#         k = (t + k) % 8

# print(k)


# k = int(input())
# n = int(input())

# for i in range(n):
#     t, z = input().split() 
#     t = int(t)
#     if (t + k) % 8 == 0:
#         k = 8
#     else:
#         k = (t + k) % 8

# print(k)

def function():
    k = int(input())
    n = int(input())

    for i in range(n):
        t, z = input().split() 
        t = int(t)
        if (t + k) % 8 == 0:
            k = 8
        else:
            k = (t + k) % 8

    print(k)

function()
