#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fp;
	char c;
	fp = fopen("file.txt", "w");
	if(fp == NULL)
	{
		printf("Error opening file!\n");
		exit(1);
	}
	printf("Enter a text (press enter to exit):\n");
	do
	{
		c = getchar();
		fputc(c, fp);
	}while(c != '\n');
	fclose(fp);
	return 0;
}
