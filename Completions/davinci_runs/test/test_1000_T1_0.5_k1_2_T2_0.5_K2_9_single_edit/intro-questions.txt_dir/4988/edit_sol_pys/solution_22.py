#include <stdio.h>

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

int main()
{
    int n, i;
    unsigned long long fact = 1;

    printf("Enter an integer: ");
    scanf("%d",&n);

    // shows error if the user enters a negative integer
    if (n < 0)
        printf("Error! Factorial of a negative number doesn't exist.");

    else
    {
        for(i=1; i<=n; ++i)
        {
            fact *= i;              // fact = fact*i;
        }
        printf("Factorial of %d = %llu", n, fact);
    }

    return 0;
}
