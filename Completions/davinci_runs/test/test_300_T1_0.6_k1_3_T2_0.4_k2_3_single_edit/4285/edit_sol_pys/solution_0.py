#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[]) {
    int fd;
    char buf[BUF_SIZE];
    int n;
    int i;

    if (argc != 2) {
        fprintf(stderr, "Usage: ./file <filename>\n");
        exit(1);
    }

    fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "open error\n");
        exit(1);
    }

    while ((n = read(fd, buf, BUF_SIZE)) > 0) {
        for (i = 0; i < n; i++) {
            if (buf[i] >= 'a' && buf[i] <= 'z') {
                buf[i] = buf[i] - 'a' + 'A';
            }
        }
        write(STDOUT_FILENO, buf, n);
    }

    if (n == -1) {
        fprintf(stderr, "read error\n");
        exit(1);
    }

    if (close(fd) == -1) {
        fprintf(stderr, "close error\n");
        exit(1);
    }

    exit(0);
}
