#include <stdio.h>


int main(void)
{
	int n, a, b;
	scanf("%d %d %d", &n, &a, &b);

	int min = n * a;
	if (b < min)
		min = b;

	printf("%d\n", min);

	return 0;
}
