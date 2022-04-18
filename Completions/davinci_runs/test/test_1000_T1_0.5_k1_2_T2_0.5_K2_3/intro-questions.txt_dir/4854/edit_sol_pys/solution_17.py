
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, c;
    cin >> n >> c;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int freq[c + 1] = {0};
    for (int i = 0; i < n; i++)
    {
        freq[arr[i]] += 1;
    }

    for (int i = 0; i < c + 1; i++)
    {
        if (freq[i] > 0)
            cout << i << ' ';
    }

    return 0;
}
