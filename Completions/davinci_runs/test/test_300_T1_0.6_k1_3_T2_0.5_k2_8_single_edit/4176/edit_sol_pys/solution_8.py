
<<<<<<< HEAD

"""
-----Notes-----

We can say that the LCM of A and B is the minimum number of snack pieces that can be evenly distributed to the guests in both of the cases.

LCM(A, B) = A × B ÷ GCD(A, B)
"""

import sys
from functools import reduce
from math import gcd
=======
#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    int a, b, c;
    cin >> a >> b;

    c = (a*b)/gcd(a,b);

    cout << c;
}
>>>>>>> 7b90e6d1e6c0d6f1f6b9d9e8d6c3f3e7b6f0c6f8
from operator import mul

def main():
    # read input
    A, B = map(int, sys.stdin.readline().split())
<<<<<<< HEAD

    # calculate LCM(A, B)
    LCM = reduce(mul, [A, B], 1) // gcd(A, B)

    # print result
    print(LCM)

if __name__ == "__main__":
    main()
