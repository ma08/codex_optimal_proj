#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <ctype.h>

//#define BUFSIZE 1024

int main(int argc, char *argv[])
{
	
	char *input;
	char *output;
	char *buffer;
	int fdIn;
	int fdOut;
	int size;
	int i;

	if(argc != 3)
	{
		printf("Error: Incorrect number of arguments.\n");
		exit(1);
	}
	else
	{
		input = argv[1];
		output = argv[2];
	}

	fdIn = open(input, O_RDONLY);

	if(fdIn < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	fdOut = open(output, O_WRONLY | O_CREAT, 0666);

	if(fdOut < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	size = lseek(fdIn, 0, SEEK_END);

	if(size < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	lseek(fdIn, 0, SEEK_SET);

	buffer = (char *)malloc(sizeof(char) * size);

	if(read(fdIn, buffer, size) < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	for(i = 0; i < size; i++)
	{
		buffer[i] = toupper(buffer[i]);
	}

	if(write(fdOut, buffer, size) < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	free(buffer);

	close(fdIn);
	close(fdOut);

	return 0;
}
