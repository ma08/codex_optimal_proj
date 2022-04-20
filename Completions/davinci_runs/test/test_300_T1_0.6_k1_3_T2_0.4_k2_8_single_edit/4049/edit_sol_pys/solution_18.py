#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int main(int argc, char *argv[])
{
    char buf[1024];
    int fd;
    int ret;

    if (argc != 2) {
        printf("Usage: %s <file>\n", argv[0]);
        exit(-1);
    }

    fd = open(argv[1], O_RDWR);
    if (fd < 0) {
        printf("open %s failed, errno: %d\n", argv[1], errno);
        exit(-1);
    }

    ret = read(fd, buf, 1024);
    printf("read %d bytes, content: %s\n", ret, buf);

    close(fd);

    return 0;
}
