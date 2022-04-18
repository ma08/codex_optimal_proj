#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fptr;
	char fname[20], str[100];
	printf("Enter file name: ");
	scanf("%s", fname);
	fptr = fopen(fname, "w");
	if (fptr == NULL)
	{
		printf("Cannot open file \n");
		exit(0);
	}
	printf("Enter a string: ");
	scanf("%[^\n]s", str);
	fprintf(fptr, "%s", str);
	fclose(fptr);
	return 0;
}
