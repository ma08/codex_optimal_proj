#include<iostream>
using namespace std;

n = int(input())
temps = list(map(int,input().split())

# sort the temperatures
temps.sort()

if all(temps[i] - temps[i-1] <= 0 for i in range(1,n)):
    print(*temps)
else:
    print("impossible")
