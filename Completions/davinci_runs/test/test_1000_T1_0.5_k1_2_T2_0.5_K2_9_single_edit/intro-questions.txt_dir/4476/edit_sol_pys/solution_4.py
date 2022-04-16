
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX_LEN 100000
# SOLUTION

import sys
import math

int main() {
    int a,b;
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        scanf("%d %d",&a,&b);
    if a == b:
        printf("0\n");
    else:
        if a % 2 == 1:
            if b % 2 == 1:
                printf("%d\n",ceil(abs(a - b) / 2));
            else:
                printf("%d\n", ceil(abs(a - b) / 2) + 1);
        else:
            if b % 2 == 1:
                printf("%d\n", ceil(abs(a - b) / 2) + 1);
            else:
                printf("%d\n", ceil(abs(a - b) / 2));
    }
    return 0;
}
