
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv) {
    int fd = open(argv[1], O_RDONLY);
    char buf[1024];
    int len = read(fd, buf, 1024);
    buf[len] = '\0';
    printf("%s\n", buf);
    close(fd);
    return 0;
}
