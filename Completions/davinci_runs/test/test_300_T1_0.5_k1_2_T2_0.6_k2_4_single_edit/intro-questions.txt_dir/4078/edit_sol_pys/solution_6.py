#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    int fd;
    int val;

    fd = open("/dev/test_chr", O_RDWR);
    if(fd < 0) {
        printf("can't open!\n");
    }

    read(fd, &val, 4);
    printf("val = %d\n", val);

    val++;
    write(fd, &val, 4);

    close(fd);

    return 0;
}
