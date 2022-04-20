

"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> l(m), r(m);
    vector<int> d(m);

    for (int i = 0; i < m; ++i) {
        cin >> l[i] >> r[i];
        d[i] = r[i] - l[i] + 1;
    }

    int maxx = 0;
    for (int i = 0; i < n; ++i) {
        maxx = max(maxx, a[i]);
    }

    vector<int> f(maxx + 1);
    for (int i = 0; i < n; ++i) {
        ++f[a[i]];
    }

    int ans = 0;
    for (int i = 0; i < m; ++i) {
        if (d[i] > f[a[l[i] - 1]]) {
            ans += d[i];
        }
    }

    cout << ans << endl;
    cout << m << endl;
    for (int i = 0; i < m; ++i) {
        cout << i + 1 << " ";
    }
    cout << endl;

    return 0;
}
"""