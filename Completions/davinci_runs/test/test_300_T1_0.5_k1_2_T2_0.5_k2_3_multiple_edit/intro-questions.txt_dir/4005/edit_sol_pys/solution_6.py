#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	const char *fname = "./test.txt";
	const char *mode = "r";
	char *buf;

	if (argc == 2)
		fname = (const char *)argv[1];

	fp = fopen((char *)fname, (char *)mode);
	if (fp == NULL) {
		perror("failed to open file");
		exit(EXIT_FAILURE);
	}

	buf = (char *)malloc(sizeof(*buf) * BUFSIZ);
	if (buf == NULL) {
		perror("failed to allocate memory");
		exit(EXIT_FAILURE);
	}
	memset((void *)buf, 0, BUFSIZ);

	while (fgets(buf, BUFSIZ, fp) != NULL)
		printf("%s", buf);

	if (fclose(fp) == EOF) {
		perror("failed to close file");
		exit(EXIT_FAILURE);
	}
	free((void *)buf);
	exit(EXIT_SUCCESS);
}
