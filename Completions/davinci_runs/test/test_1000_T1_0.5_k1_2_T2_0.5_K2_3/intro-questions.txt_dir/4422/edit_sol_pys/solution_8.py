#include <stdio.h>
#include <string.h>

n, k = map(int, input().split())
char s[100];
scanf("%s",&s);
print(s[:k-1] + s[k-1].lower() + s[k:]) 
