#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <errno.h>
#include <dirent.h>

int main(){
    int fd = open("file.txt", O_RDONLY);
    char *arr = (char *)calloc(sizeof(char), 10);
    int size = read(fd, arr, 10);
    printf("%d\n", size);
    printf("%s\n", arr);
    free(arr);
    close(fd);
    return 0;
}
