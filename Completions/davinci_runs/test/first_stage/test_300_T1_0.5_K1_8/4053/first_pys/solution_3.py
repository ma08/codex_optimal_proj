


# Solution

#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, n) for (int i = 1; i < (n); ++i)
using namespace std;
typedef long long ll;
const ll INF = 1LL << 60;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<string> vec(2*n-2);
    rep(i, 2*n-2) cin >> vec[i];

    vector<string> s;
    vector<string> t;

    rep(i, 2*n-2){
        if(vec[i].size() == n-1){
            s.push_back(vec[i]);
        }
        else t.push_back(vec[i]);
    }

    rep(i, 2*n-2){
        if(i < n-1) cout << 'P';
        else cout << 'S';
    }
    cout << endl;

    return 0;
}