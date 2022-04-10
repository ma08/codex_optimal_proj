#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
#include <sstream>
#include <complex>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <numeric>
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> P;
#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define mod2 998244353
#define MAX 200000
#define int long long
template <class T>
inline bool chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
        return true;
    }
    return false;
}
template <class T>
inline bool chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
        return true;
    }
    return false;
}
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int lcm(int a, int b) { return a / gcd(a, b) * b; }
int ceil(int a, int b) { return (a + b - 1) / b; }
int digitlen(int n) { return ceil(log10(n)); }
int digit(int n, int k) { return (n / pow(10, k - 1)) % 10; }
int digitcount(int n) { return digitlen(n) * 9; }
int digitcount(int n, int k) { return digitlen(n) * (k - 1); }
int digitfirst(int n) { return n / pow(10, digitlen(n) - 1); }
int digitlast(int n) { return n % 10; }
int bitcount(int n)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n = n & (n - 1);
    }
    return ret;
}
int bitfirst(int n)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n = n >> 1;
    }
    return ret;
}
int bitlast(int n)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n = (n & (n - 1));
    }
    return ret;
}
int bitcount(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret += n % k;
        n /= k;
    }
    return ret;
}
int bitfirst(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n /= k;
    }
    return ret;
}
int bitlast(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n %= k;
    }
    return ret;
}
int digitcount(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret += n % k;
        n /= k;
    }
    return ret;
}
int digitfirst(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n /= k;
    }
    return ret;
}
int digitlast(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n %= k;
    }
    return ret;
}
int bitcount(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret += n % k;
        n /= k;
    }
    return ret;
}
int bitfirst(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n /= k;
    }
    return ret;
}
int bitlast(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n %= k;
    }
    return ret;
}
int digitcount(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret += n % k;
        n /= k;
    }
    return ret;
}
int digitfirst(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n /= k;
    }
    return ret;
}
int digitlast(int n, int k)
{
    int ret = 0;
    while (n)
    {
        ret++;
        n %= k;
    }
    return ret;
}
