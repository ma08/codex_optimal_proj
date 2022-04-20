
#include<stdio.h>
int main(void)
{
    int n,a[100],i,j,k,count=1,max=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]<a[j])
            {
                k=a[i];
                a[i]=a[j];
                a[j]=k;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if((a[i]%a[j]==0)||(a[j]%a[i]==0))
            {
                count++;
            }
        }
        if(count>max)
        {
            max=count;
        }
    }
    printf("%d",max);

    return 0;
}
