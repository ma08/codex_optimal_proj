#include <stdio.h>
#include <stdlib.h>

void main() {
	FILE *fp;
	char ch;
	int i;
	fp = fopen("file.txt", "w");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(1);
	}
	printf("Enter text, press # to exit\n");
	while ((ch = getchar()) != '#') {
		fputc(ch, fp);
	}
	fclose(fp);
	fp = fopen("file.txt", "r");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(1);
	}
	printf("Contents of file.txt\n");
	while ((ch = fgetc(fp)) != EOF) {
		putchar(ch);
	}
	fclose(fp);
}
