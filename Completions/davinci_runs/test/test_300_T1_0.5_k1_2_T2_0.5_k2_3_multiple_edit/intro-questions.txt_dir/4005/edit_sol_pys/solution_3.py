#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	char *fname = "./test.txt", *mode = "r";
	char *buf;

	if (argc == 2)
		fname = argv[1];

	fp = fopen(fname, mode);
	if (fp == NULL) {
		perror("failed to open file");
		exit(EXIT_FAILURE);
	}	

	buf = (char *)malloc(sizeof(char) * BUFSIZ);
	if (buf == NULL) {
		perror("failed to allocate memory");
		exit(EXIT_FAILURE);
	}
	memset(buf, 0, BUFSIZ);

	while (fgets(buf, BUFSIZ, fp) != NULL)
		printf("%s", buf);

	if (fclose(fp) == EOF) {
		perror("failed to close file");
		exit(EXIT_FAILURE);
	}	
	free(buf);
	exit(EXIT_SUCCESS);
}
