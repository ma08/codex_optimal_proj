#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(){

	printf("\nThis is the first line\n");
	int fd = open("test.txt", O_CREAT | O_RDWR, 0777);
	if(fd < 0)
		printf("Error opening file\n");
	else
		printf("Success opening file\n");

	int w = write(fd, "This is a test\n", 15);
	if(w < 0)
		printf("Error writing file\n");
	else
		printf("Success writing file\n");
	close(fd);	

	int fd2 = open("test.txt", O_RDONLY);
	if(fd2 < 0)
		printf("Error opening file\n");
	else
		printf("Success opening file\n");

	char *buf = (char *)malloc(16);
	int r = read(fd2, buf, 15);
	if(r < 0)
		printf("Error reading file\n");
	else
		printf("Success reading file\n");

	printf("%s\n", buf);
	close(fd2);
	free(buf);
	return 0;
}
