#include <iostream>

#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
    int d, t, s;
    scanf("%d %d %d", &d, &t, &s);
    if (d / s <= t) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}
