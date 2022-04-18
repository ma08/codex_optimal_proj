
#include<iostream>
using namespace std;
int main(){
    int n,k,c=0;
    cin >> n >> k;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(a[i] > a[j]){
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    for(int i = 0; i < n; i++){
        if(a[i] != a[i + 1]){
            c++;
        }
        if(c==k){
            cout<<a[i];
            break;
        }
    }
    return 0;
}
