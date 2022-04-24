#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	int i, j;
	char ch;
	char str[100];
	char *p;
	char *q;
	char *r;
	fp = fopen("file.c", "r");
	if (fp == NULL) {
		printf("Open file failed\n");
		exit(0);
	}
	while (fgets(str, 100, fp) != NULL) {
		p = str;
		while (*p != '\0') {
			if (*p == '\t') {
				for (i = 0; i < 4; i++) {
					printf(" ");
				}
			} else {
				printf("%c", *p);
			}
			p++;
		}
	}
	fclose(fp);
	return 0;
}
