#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int main(int argc, char *argv[]) {

	char *filename = argv[1];
	int fd = open(filename, O_RDWR);
	
	if (fd == -1) {
		printf("error opening file: %s\n", strerror(errno));
		exit(1);
	}
	
	printf("file opened successfully\n");
	
	char *buf = malloc(sizeof(char) * 1024);
	int bytes_read = read(fd, buf, 1024);
	
	if (bytes_read == -1) {
		printf("error reading file: %s\n", strerror(errno));
		exit(1);
	}
	
	printf("%s\n", buf);
	
	char *new_buf = "hello world!\n";
	int bytes_written = write(fd, new_buf, strlen(new_buf));
	
	if (bytes_written == -1) {
		printf("error writing to file: %s\n", strerror(errno));
		exit(1);
	}
	
	printf("file written to successfully\n");
	
	close(fd);
	
	return 0;
}
