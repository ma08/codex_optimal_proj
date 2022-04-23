#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int a[n*n];
    for(int i=0;i<n*n;i++)
        cin>>a[i];

    if (n == 1)
    {
        cout<<"YES\n";
        cout<<a[0];
    }
    else:
        set<int> s;
        for(int i=0;i<n*n;i++)
            s.insert(a[i]);
        if (s.size() != n*n)
        {
            cout<<"NO\n";
        }
        else
        {
            int n1 = n/2;
            int n2 = n-n1;
            int a1[n1*n1];
            int a2[n2*n2];
            for(int i=0;i<n1*n1;i++)
                a1[i] = a[i];
            for(int i=0;i<n2*n2;i++)
                a2[i] = a[n1*n1+i];
            sort(a1,a1+n1*n1);
            sort(a2,a2+n2*n2);
            reverse(a2,a2+n2*n2);
            if(equal(a1,a1+n1*n1,a2))
            {
                cout<<"YES\n";
                for(int i=0;i<n;i++)
                {
                    for(int j=0;j<n;j++)
                        cout<<a[i*n+j]<<" ";
                    cout<<"\n";
                }
            }
            else
            {
                cout<<"NO\n";
            }
        }
    }
    return 0;
}
