
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int> left(n), right(n);
    left[0] = a[0];
    right[n - 1] = a[n - 1];
    for (int i = 1; i < n; i++) {
        left[i] = max(left[i - 1], a[i]);
        right[n - i - 1] = max(right[n - i], a[n - i - 1]);
    }

    string ans = "";
    for (int i = 0; i < n; i++) {
        if (left[i] == max(left[i], right[i])) {
            ans += "1";
        } else {
            ans += "2";
        }
    }
    cout << ans << endl;
}


# SOLUTION
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

# get the left and right k-th max elements
for i in range(1, n):
    left[i] = max(left[i-1], a[i-1])
    right[n-i-1] = max(right[n-i], a[n-i])

ans = [0] * n
for i in range(n):
    if left[i] == max(left[i], right[i]):
        ans[i] = 1
    else:
        ans[i] = 2

print("".join(map(str, ans)))
