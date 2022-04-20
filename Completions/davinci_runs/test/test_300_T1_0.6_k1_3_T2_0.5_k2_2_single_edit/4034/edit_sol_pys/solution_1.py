
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n, i, j, a, b, x, y, z;
  cin >> n;
  int arr[n];
  for (i = 0; i < n; i++)
    cin >> arr[i];
  int count = 0;
  for (i = 0; i < n; i++)
  {
    for (j = i + 1; j < n; j++)
    {
      if (arr[i] > arr[j])
      {
        count++;
      }
    }
  }
  cout << count;
  return 0;
}
