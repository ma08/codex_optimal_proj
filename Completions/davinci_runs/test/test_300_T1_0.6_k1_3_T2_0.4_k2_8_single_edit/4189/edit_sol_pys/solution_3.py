#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
    int fd;
    struct stat st;
    char *type, *readok;

    if (argc != 2) {
        fprintf(stderr, "usage: %s <filename>\n", argv[0]);
        exit(1);
    }

    if (lstat(argv[1], &st) < 0) {
        perror(argv[1]);
        exit(1);
    }

    if (S_ISREG(st.st_mode))
        type = "regular";
    else if (S_ISDIR(st.st_mode))
        type = "directory";
    else
        type = "other";

    if ((st.st_mode & S_IRUSR))
        readok = "yes";
    else
        readok = "no";

    printf("type: %s, read: %s\n", type, readok);

    exit(0);
}
