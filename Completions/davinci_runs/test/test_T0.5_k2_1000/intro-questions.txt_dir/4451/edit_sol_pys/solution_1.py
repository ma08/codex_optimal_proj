#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp = NULL;
	char str[100];
	fp = fopen("file.txt", "r");
	if (fp == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	while(fgets(str, 100, fp) != NULL)
	{
		printf("%s", str);
	}
	fclose(fp);
	return 0;
}
