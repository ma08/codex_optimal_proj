

#include<stdio.h>

int main(){
    int n,i,a[100];
    scanf("%d",&n);

n = int(input())
a = list(map(int,input().split()))

g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])

print(g)
