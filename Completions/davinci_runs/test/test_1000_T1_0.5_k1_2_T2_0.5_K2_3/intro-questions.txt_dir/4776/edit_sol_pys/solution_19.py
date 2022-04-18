

#include <iostream>

using namespace std;

int main()
{
    int n, s, t, days[365] = {0}, maxDays = 0;
    cin >> n;
    while (n--)
    {
        cin >> s >> t;
        for (int i = s - 1; i < t; i++)
        {
            days[i]++;
            if (maxDays < days[i])
            {
                maxDays = days[i];
            }
        }
    }
    cout << maxDays << endl;
}
