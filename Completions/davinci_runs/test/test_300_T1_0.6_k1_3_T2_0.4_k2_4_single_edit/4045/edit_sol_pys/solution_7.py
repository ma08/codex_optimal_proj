#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUF_SIZE 1024
#define STD_INPUT 0
#define STD_OUTPUT 1

int main(int argc, char* argv[])
{
	char buf[BUF_SIZE];
	int fd;
	int n;
	int i;

	if(argc < 2)
	{
		fprintf(stderr, "Usage: %s filename\n", argv[0]);
		exit(1);
	}

	if((fd = open(argv[1], O_RDONLY)) == -1)
	{
		fprintf(stderr, "open error for %s\n", argv[1]);
		exit(1);
	}

	while((n = read(fd, buf, BUF_SIZE)) > 0)
	{
		for(i = 0; i < n; i++)
			buf[i] = toupper(buf[i]);
		if(write(STDOUT_FILENO, buf, n) != n)
		{
			fprintf(stderr, "write error\n");
			exit(1);
		}
	}

	if(n < 0)
	{
		fprintf(stderr, "read error\n");
		exit(1);
	}

	exit(0);
}
