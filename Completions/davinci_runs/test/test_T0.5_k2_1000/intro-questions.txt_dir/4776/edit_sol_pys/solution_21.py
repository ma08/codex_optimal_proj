
#include <iostream>
#include <algorithm> // max

using namespace std;

int main()
{
    int N, s, t, days[365] = {0}, max_days = 0; // s: start, t: end
    cin >> N;
    while (N--)
    {
        cin >> s >> t;
        for (int i = s - 1; i < t; i++)
        {
            days[i]++;
            max_days = max(max_days, days[i]);
        }
    }
    cout << max_days << endl;
}
