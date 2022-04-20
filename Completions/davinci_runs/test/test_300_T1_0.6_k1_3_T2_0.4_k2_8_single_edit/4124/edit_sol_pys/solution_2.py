#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
	int fd, fd2;
	char buf[1024];
	ssize_t size;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s <file>\n", argv[0]);
		exit(1);
	}

	fd = open(argv[1], O_RDONLY);
	if (fd < 0) {
		fprintf(stderr, "open() failed: %s\n", strerror(errno));
		exit(1);
	}

	fd2 = dup(fd);
	if (fd2 < 0) {
		fprintf(stderr, "dup() failed: %s\n", strerror(errno));
		exit(1);
	}

	size = read(fd, buf, sizeof(buf));
	if (size < 0) {
		fprintf(stderr, "read() failed: %s\n", strerror(errno));
		exit(1);
	}

	printf("fd = %d\n", fd);
	printf("fd2 = %d\n", fd2);

	fprintf(stdout, "%.*s", (int)size, buf);
	return 0;
}
