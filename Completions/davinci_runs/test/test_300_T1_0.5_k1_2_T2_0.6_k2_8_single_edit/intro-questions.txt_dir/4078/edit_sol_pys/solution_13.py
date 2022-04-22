#include <stdio.h>

int main()
{
	FILE *fp;
	char ch;
	fp = fopen("file.c", "r");
	
	if (fp == NULL)
	{
		printf("Error opening file\n");
		return -1;
	}
	while (1)
	{
		ch = fgetc(fp);
		if(ch == EOF)
			break;
		printf("%c", ch);
	}
	fclose(fp);
	return 0;
}
