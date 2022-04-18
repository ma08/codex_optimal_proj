
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
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

for i in range(c + 1):
    if freq[i] > 0:
        print((str(i) + ' ') * freq[i], end='')
