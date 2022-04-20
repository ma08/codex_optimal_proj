#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

#define MAX_BUF 1024

int main(int argc, char *argv[])
{
    int fd, len;
    char buf[MAX_BUF];

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        exit(1);
    }

    if ((fd = open(argv[1], O_RDONLY)) < 0) {
        fprintf(stderr, "open error for %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    while ((len = read(fd, buf, MAX_BUF)) > 0) {
        write(STDOUT_FILENO, buf, len);
    }

    close(fd);

    return 0;
}
