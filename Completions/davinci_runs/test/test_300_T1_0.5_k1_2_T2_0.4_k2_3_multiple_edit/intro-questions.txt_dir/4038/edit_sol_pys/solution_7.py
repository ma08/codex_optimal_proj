#include <bits/stdc++.h>
using namespace std;

int main() {
    int n = int(input());
    vector<int> a(n*n);
    for(int i = 0; i < n*n; i++) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << "YES" << endl;
        cout << a[0] << endl;
    }
    else:
        if (set(a).size() != n*n) {
            cout << "NO" << endl;
        } else {
            int n1 = n/2;
            int n2 = n-n1;
            vector<int> a2(a.begin()+n1*n1, a.end());
            vector<int> a1(a.begin(), a.begin()+n1*n1);
            sort(a1.begin(), a1.end());
            sort(a2.begin(), a2.end());
            reverse(a2.begin(), a2.end());
            if (a1 == a2) {
                cout << "YES" << endl;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        cout << a[i*n+j] << " ";
                    }
                    cout << endl;
                }
            } else {
                cout << "NO" << endl;
            }
        }
    }

    return 0;
}
        else:
            print('NO')
