
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <cstdlib>
#include <fstream>
#include <queue>
#include <stack>
#include <random>
#include <deque>
#include <bitset>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
using namespace std;
#define ll long long
#define ld long double
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define ps(x) cout << x << " "
#define pl(x) cout << x << endl
#define nl cout << endl
#define con continue
#define MOD 1000000007
#define int long long
#define double long double
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vl vector<ll>
#define vi vector<int>
#define vpl vector<pll>
#define vpi vector<pii>
#define vvi vector<vi>
#define vvl vector<vl>
#define inf 999999999999999
#define sz(x) (int)(x).size()
#define fr(i, a, b) for (int i = a; i < b; i++)
#define frn(i, a, b) for (int i = a; i > b; i--)
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define ps(x) cout << x << " "
#define pl(x) cout << x << endl
#define nl cout << endl
#define con continue
#define MOD 1000000007
#define int long long
#define double long double
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vl vector<ll>
#define vi vector<int>
#define vpl vector<pll>
#define vpi vector<pii>
#define vvi vector<vi>
#define vvl vector<vl>
#define inf 999999999999999
#define sz(x) (int)(x).size()
#define fr(i, a, b) for (int i = a; i < b; i++)
#define frn(i, a, b) for (int i = a; i > b; i--)
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define ps(x) cout << x << " "
#define pl(x) cout << x << endl
#define nl cout << endl
#define con continue
#define MOD 1000000007
#define int long long
#define double long double
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vl vector<ll>
#define vi vector<int>
#define vpl vector<pll>
#define vpi vector<pii>
#define vvi vector<vi>
#define vvl vector<vl>
#define inf 999999999999999
#define sz(x) (int)(x).size()
#define fr(i, a, b) for (int i = a; i < b; i++)
#define frn(i, a, b) for (int i = a; i > b; i--)
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define ps(x) cout << x << " "
#define pl(x) cout << x << endl
#define nl cout << endl
#define con continue
#define MOD 1000000007
#define int long long
#define double long double
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vl vector<ll>
#define vi vector<int>
#define vpl vector<pll>
#define vpi vector<pii>
#define vvi vector<vi>
#define vvl vector<vl>
#define inf 999999999999999
#define sz(x) (int)(x).size()
#define fr(i, a, b) for (int i = a; i < b; i++)
#define frn(i, a, b) for (int i = a; i > b; i--)
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define all(something) something.begin(), something.end()
#define rall(something) something.rbegin(), something.rend()
#define siz(container) (int)container.size()
#define int long long
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define mp make_pair
#define ff first


n = int(input())
s = input()

if n == 1:
    print(1)
    print(1)
    exit()

if n == 2:
    if s[0] > s[1]:
        print(2)
        print(1, 2)
    else:
        print(1)
        print(1)
    exit()

c = [1] * n

if s[0] > s[1]:
    c[0] = 2

if s[n - 1] < s[n - 2]:
    c[n - 1] = 2

for i in range(1, n - 1):
    if s[i] > s[i + 1]:
        c[i] = max(c[i], c[i + 1])
        c[i + 1] = max(c[i], c[i + 1])
    if s[i] < s[i - 1]:
        c[i] = max(c[i], c[i - 1])
        c[i - 1] = max(c[i], c[i - 1])

print(max(c))
print(*c)
