

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, s, t, days[365] = {0}, max_days = 0, i;
    cin >> N;
    while (N--)
    {
        cin >> s >> t;
        for (i = s - 1; i < t; i++)
        {
            days[i]++;
            max_days = max(max_days, days[i]);
        }
    }
    cout << max_days << endl;
}
