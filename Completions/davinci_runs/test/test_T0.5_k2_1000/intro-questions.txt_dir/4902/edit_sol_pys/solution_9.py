
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>

#define INFI 1e18+7
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long ll;

using namespace std;

int n;
int a[200001];

int solve() {
  int res = 0;
  int l = 0;
  int r = n-1;
  while (l < r) {
    if (a[l] == a[r]) {
      l++;
      r--;
    } else if (a[l] < a[r]) {
      a[l+1] += a[l];
      res++;
      l++;
    } else {
      a[r-1] += a[r];
      res++;
      r--;
    }
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
  int t;
  cin >> t;
  while (t--) {
    cin >> n;
    for (int i=0;i<n;i++) cin >> a[i];
    cout << solve() << endl;
  }
  return 0;
}
