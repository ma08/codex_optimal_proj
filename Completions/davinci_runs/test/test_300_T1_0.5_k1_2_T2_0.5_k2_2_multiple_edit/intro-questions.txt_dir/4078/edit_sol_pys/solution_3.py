#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
	char *src;
	char *dst;
	int fd1, fd2, ret;
	char buf[0x100];
	int len;
	
	if (argc != 3) {
		printf("usage: %s src dst\n", argv[0]);
		return -1;
	}
	
	src = argv[1];
	dst = argv[2];
	
	fd1 = open(src, O_RDONLY);
	if (fd1 < 0) {
		printf("open %s error\n", src);
		return -1;
	}
	
	fd2 = open(dst, O_WRONLY | O_CREAT, 0644);
	if (fd2 < 0) {
		printf("open %s error\n", dst);
		return -1;
	}
	
	while (1) {
		len = read(fd1, buf, 0x100);
		if (len <= 0) {
			break;
		}
		
		ret = write(fd2, buf, len);
		if (ret != len) {
			printf("write error\n");
			break;
		}
	}
	
	close(fd1);
	close(fd2);
	
	return 0;
}
