#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define MAX_SIZE 1024

int main(int argc, char *argv[])
{
	//Check to see if there are 2 arguments
	if(argc != 2)
	{
		fprintf(stderr, "Usage: %s <file>\n", argv[0]);
		exit(1);
	}

	//Open file and check for error
	int fd = open(argv[1], O_RDONLY);
	if(fd < 0)
	{
		fprintf(stderr, "%s: %s: %s\n", argv[0], argv[1], strerror(errno));
		exit(1);
	}

	//Read from file and check for error
	char buf[MAX_SIZE];
	int n = read(fd, buf, MAX_SIZE);
	if(n < 0)
	{
		fprintf(stderr, "%s: %s: %s\n", argv[0], argv[1], strerror(errno));
		exit(1);
	}

	//Write to stdout and check for error
	int w = write(1, buf, n);
	if(w < 0)
	{
		fprintf(stderr, "%s: %s: %s\n", argv[0], argv[1], strerror(errno));
		exit(1);
	}

	//Close file and check for error
	int c = close(fd);
	if(c < 0)
	{
		fprintf(stderr, "%s: %s: %s\n", argv[0], argv[1], strerror(errno));
		exit(1);
	}

	return 0;
}
