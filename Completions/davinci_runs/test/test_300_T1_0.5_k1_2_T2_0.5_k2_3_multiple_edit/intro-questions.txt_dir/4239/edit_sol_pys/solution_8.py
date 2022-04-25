#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[])
{
	char *file_name = argv[1];
	FILE *fp = fopen(file_name, "r");
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	if (fp == NULL) exit(EXIT_FAILURE);
	while ((read = getline(&line, &len, fp)) != -1)
	{
		printf("Retrieved line of length %zu :\n", read);
		printf("%s", line);
	}
	free(line);
	fclose(fp);
	return 0;
}
