

#SOLUTION

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

long long gcd(long long a, long long b) {
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

int main() {
    long long a, b;
    cin >> a >> b;
    long long c = gcd(a, b);
    a /= c;
    b /= c;
    long long side = max(a, b);
    long long perimeter = 2 * (a + b);
    long long answer = side * perimeter;
    cout << answer;
    return 0;
}