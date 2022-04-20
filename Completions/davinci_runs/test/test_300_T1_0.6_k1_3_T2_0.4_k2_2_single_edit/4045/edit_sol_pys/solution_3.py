#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[])
{
	int fd_src, fd_dest;
	ssize_t ret_in, ret_out;
	char buffer[BUFFER_SIZE];
	char *src_file = argv[1];
	char *dest_file = argv[2];

	if (argc != 3) {
		printf("Usage: %s <source_file> <dest_file>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	/* Open source file for reading */
	fd_src = open(src_file, O_RDONLY);
	if (fd_src < 0) {
		printf("Error: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	/* Open destination file for writing */
	fd_dest = open(dest_file, O_WRONLY | O_CREAT, 0644);
	if (fd_dest < 0) {
		printf("Error: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	/* Copy data from source file to destination file */
	while ((ret_in = read(fd_src, &buffer, BUFFER_SIZE)) > 0) {
		ret_out = write(fd_dest, &buffer, (ssize_t) ret_in);
		if (ret_out != ret_in) {
			printf("Error: %s\n", strerror(errno));
			exit(EXIT_FAILURE);
		}
	}

	/* Close files */
	close(fd_src);
	close(fd_dest);

	exit(EXIT_SUCCESS);
}
