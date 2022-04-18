#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUF_SIZE 10

int main(int argc, char *argv[])
{
    int fd;
    char buf[BUF_SIZE];
    ssize_t numRead;

    if (argc != 2 || strcmp(argv[1], "--help") == 0) {
        printf("%s file\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        printf("open file failed\n");
        exit(EXIT_FAILURE);
    }

    while ((numRead = read(fd, buf, BUF_SIZE)) > 0) {
        if (write(STDOUT_FILENO, buf, numRead) != numRead) {
            printf("couldn't write whole buffer\n");
            exit(EXIT_FAILURE);
        }
    }

    if (numRead == -1) {
        printf("read file failed\n");
        exit(EXIT_FAILURE);
    }

    if (close(fd) == -1) {
        printf("close file failed\n");
        exit(EXIT_FAILURE);
    }

    return 0;
}
