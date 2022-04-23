
N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
dist = 0
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break

"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int N, X;
    cin >> N >> X;
    vector<int> L(N);
    for (int i = 0; i < N; i++) {
        cin >> L[i];
    }

    int cnt = 1;
    int dist = 0;
    for (int i = 0; i < N; i++) {
        dist += L[i];
        if (dist <= X) {
            cnt++;
        } else {
            break;
        }
    }


    cout << cnt << endl;
    return 0;
}
"""
print(cnt)
