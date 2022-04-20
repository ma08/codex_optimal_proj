#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[])
{
	FILE *fp;
	char buffer[BUFFER_SIZE];
	int count;

	if(argc != 2)
	{
		fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
		return 1;
	}

	fp = fopen(argv[1], "r");
	if(fp == NULL)
	{
		fprintf(stderr, "fopen error for %s\n", argv[1]);
		return 1;
	}

	while((count = fread(buffer, 1, BUFFER_SIZE, fp)) > 0)
	{
		if(fwrite(buffer, 1, count, stdout) != count)
		{
			fprintf(stderr, "fwrite error\n");
			return 1;
		}
	}

	if(ferror(fp))
	{
		fprintf(stderr, "fread error\n");
		return 1;
	}

	fclose(fp);
	return 0;
}
