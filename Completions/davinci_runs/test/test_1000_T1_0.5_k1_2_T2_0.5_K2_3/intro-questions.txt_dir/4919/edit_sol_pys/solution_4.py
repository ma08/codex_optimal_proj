#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, vector<string>> trips;
    for (int i = 0; i < n; i++) {
        string country, year;
        cin >> country >> year;
        trips[country].push_back(year);
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        string country;
        int k;
        cin >> country >> k;
        cout << trips[country][k - 1] << endl;
    }
    return 0;
}
