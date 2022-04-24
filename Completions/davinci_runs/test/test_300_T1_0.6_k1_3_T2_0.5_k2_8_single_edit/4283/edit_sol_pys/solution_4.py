
#include <iostream>
#include<vector>
#include<algorithm>
#include <string>
#include <list>
#include <cmath>
#include <iomanip>
#include <stack>
#include <queue>
#include <utility>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
typedef long long ll;
#define INF 1000000007
int main(void){
    int n;
    int a[100000];
    cin >> n;
    REP(i,n){
        cin >> a[i];
    }
    sort(a,a+n);
    int count = 1;
    for(int i=1; i<n; ++i){
        if(abs(a[i]-a[i-1]) <= 5){
            count++;
        }else{
            break;
        }
    }
    for(int i=n-2; i>=0; --i){
        if(abs(a[i]-a[i+1]) <= 5){
            count++;
        }else{
            break;
        }
    }
    cout << count << endl;
    return 0;
}
