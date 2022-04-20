#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	FILE *fp;
	char c;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s <file>\n", argv[0]);
		return 1;
	}

	fp = fopen(argv[1], "r");

	if (fp == NULL) {
		fprintf(stderr, "Cannot open %s\n", argv[1]);
		return 1;
	}

	while ((c = fgetc(fp)) != EOF)
		putchar(c);

	fclose(fp);

	return 0;
}
