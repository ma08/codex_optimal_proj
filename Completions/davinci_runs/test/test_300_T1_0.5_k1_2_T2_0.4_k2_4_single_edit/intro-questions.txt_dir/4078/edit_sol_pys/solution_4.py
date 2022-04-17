#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <errno.h>

int main(int argc, char *argv[]) {

  if (argc != 2) {
    printf("ERROR: Invalid number of arguments\n");
    return 1;
  }

  char *path = argv[1];
  struct stat file;
  if (stat(path, &file) == -1) {
    printf("ERROR: %s\n", strerror(errno));
    return 1;
  }

  if (S_ISDIR(file.st_mode)) {
    printf("%s is a directory\n", path);
  } else if (S_ISREG(file.st_mode)) {
    printf("%s is a regular file\n", path);
  } else {
    printf("%s is not a regular file or directory\n", path);
  }

  return 0;
}
