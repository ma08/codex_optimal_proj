#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	char str[100];
	fp = fopen("file.txt", "w");
	if (fp == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	printf("Enter the string to be written to the file\n");
	fgets(str, 100, stdin); //fgets(str, sizeof(str), stdin);
	fprintf(fp, "%s", str);
	fclose(fp);
	return 0;
}
