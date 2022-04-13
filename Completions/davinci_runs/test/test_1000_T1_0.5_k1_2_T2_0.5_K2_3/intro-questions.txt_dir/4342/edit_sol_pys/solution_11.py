
```cpp
### Solution

#include <bits/stdc++.h>
using namespace std;

const int N = 200000 + 10;

int n, a[N];
vector<int> g[N];

void dfs(int u, int p, int &red, int &blue, int &uncolored) {
	red += (a[u] == 1);
	blue += (a[u] == 2);
	uncolored += (a[u] == 0);
	for (int v : g[u]) {
		if (v == p) continue;
		dfs(v, u, red, blue, uncolored);
	}
}

int main() {
	int ans = 0;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	for (int i = 1; i < n; i++) {
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	for (int u = 1; u <= n; u++) {
		for (int v : g[u]) {
			int red = 0, blue = 0, uncolored = 0;
			dfs(u, v, red, blue, uncolored);
			int red1 = 0, blue1 = 0, uncolored1 = 0;
			dfs(v, u, red1, blue1, uncolored1);
			if (red && blue1) continue;
			if (red1 && blue) continue;
			ans++;
		}
	}
	cout << ans << endl;
	return 0;
}
```
