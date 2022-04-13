
a,b=map(int,input().split())
c,d=map(int,input().split())
t=int(input())

# If the start and end points are the same, then we can do a U-turn and get there.
if a == c and b == d:
    print("Y")

# If we are trying to travel more than t units, we can't get there.
if abs(a-c) + abs(b-d) > t:
    print("N")

# If we are trying to travel less than t units, we can't get there. 
if abs(a-c) + abs(b-d) < t:
    print("N")

# If we are trying to travel exactly t units, we can get there.
if abs(a-c) + abs(b-d) == t:
    print("Y")
