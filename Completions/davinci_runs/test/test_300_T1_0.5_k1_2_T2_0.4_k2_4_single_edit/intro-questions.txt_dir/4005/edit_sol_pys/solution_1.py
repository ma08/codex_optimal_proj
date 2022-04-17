#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>

int main(int argc, char *argv[]) {
  int fd = open(argv[1], O_RDONLY);
  if (fd == -1) {
    printf("error %d: %s\n", errno, strerror(errno));
    return 0;
  }
  struct stat *buf = malloc(sizeof(struct stat));
  fstat(fd, buf);
  printf("File Size: %d bytes\n", buf->st_size);
  printf("Mode: %o\n", buf->st_mode);
  printf("Time of Last Access: %s\n", ctime(&buf->st_atime));
  return 0;
}
