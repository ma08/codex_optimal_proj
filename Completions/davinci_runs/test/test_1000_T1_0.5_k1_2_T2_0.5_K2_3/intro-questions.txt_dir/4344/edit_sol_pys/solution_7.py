#include<iostream>
using namespace std;
void sort(int a[],int n){
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(a[i]>a[j]){
                int temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}
int main(){
    int n,k;
    cin>>n>>k;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a,n);
    int c=0;
    for(int i=0;i<n-1;i++){
        if(a[i]!=a[i+1]){
            c++;
        }
        if(c==k){
            cout<<a[i];
            break;
        }
    }
    return 0;
}
