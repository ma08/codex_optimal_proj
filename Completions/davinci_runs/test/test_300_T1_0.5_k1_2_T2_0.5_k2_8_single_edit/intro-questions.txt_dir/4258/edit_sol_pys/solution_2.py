#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define MAX_SIZE 1024

int main(int argc, char **argv)
{
	int fd;
	char buf[MAX_SIZE];
	int ret;
	char *file_name;
	int flags;
	mode_t mode;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s file_name\n", argv[0]);
		exit(1);
	}

	file_name = argv[1];
	flags = O_WRONLY | O_CREAT | O_TRUNC;
	mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;

	fd = open(file_name, flags, mode);
	if (fd < 0) {
		fprintf(stderr, "open() failed\n");
		exit(1);
	}

	while (1) {
		ret = read(STDIN_FILENO, buf, MAX_SIZE);
		if (ret == 0)
			break;
		write(fd, buf, ret);
	}

	close(fd);
	return 0;
}
