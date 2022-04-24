

#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int count = 0;
	while(n > 0) {
		if(n % 10 == 0) {
			n /= 10;
		} else {
			n++;
		}
		count++;
	}
	printf("%d\n", count);
	return 0;
}

import sys

n = int(sys.stdin.readline())

def f(x):
    while x % 10 == 0:
        x //= 10
    return x + 1

reachable = set()

def solve(x):
    if x in reachable:
        return
    reachable.add(x)
    solve(f(x))

solve(n)

print(len(reachable))
