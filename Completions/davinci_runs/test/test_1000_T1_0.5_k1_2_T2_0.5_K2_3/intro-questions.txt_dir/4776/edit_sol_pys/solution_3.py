
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, s, t, days[365] = {0}, maxDays = 0;
    cin >> N;
    while (N--)
    {
        cin >> s >> t;
        for (int i = s - 1; i < t; i++)
        {
            days[i]++;
            maxDays = max(maxDays, days[i]);
        }
    }
    cout << maxDays << endl;
}
