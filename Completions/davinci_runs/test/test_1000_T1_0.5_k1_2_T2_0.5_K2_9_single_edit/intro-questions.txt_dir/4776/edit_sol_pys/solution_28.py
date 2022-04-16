
#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int n, s, t, days[365] = {0}, max_days = 0;
    cin >> n;
    while (n--)
    {
        cin >> s >> t;
        for (int i = s; i < t; i++)
        {
            days[i]++;
            max_days = max(max_days, days[i]);
        }
    }
    cout << max_days << endl;
    return 0;
}
