#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int d[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &d[i]);
    }

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break
print(n//2 + cnt)
