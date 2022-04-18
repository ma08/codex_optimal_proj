#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0)
    {
        fprintf(stderr, "Error opening file %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    struct stat st;
    if (fstat(fd, &st) < 0)
    {
        fprintf(stderr, "Error statting file %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    printf("File %s is %lu bytes\n", argv[1], st.st_size);

    char *buf = malloc(st.st_size);
    if (!buf)
    {
        fprintf(stderr, "Error allocating memory: %s\n", strerror(errno));
        exit(1);
    }

    if (read(fd, buf, st.st_size) != st.st_size)
    {
        fprintf(stderr, "Error reading file %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    close(fd);

    printf("%s\n", buf);

    free(buf);
}
