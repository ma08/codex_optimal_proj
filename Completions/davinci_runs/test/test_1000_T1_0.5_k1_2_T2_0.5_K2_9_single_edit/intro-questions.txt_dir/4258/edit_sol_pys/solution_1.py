#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
  if (argc < 2) {
    printf("Please provide a filename.\n");
    exit(1);
  }
  char *filename = argv[1];
  int fd = open(filename, O_RDONLY);
  if (fd == -1) {
    printf("Could not open file.\n");
    exit(1);
  }
  struct stat fileStats;
  fstat(fd, &fileStats);
  printf("File Size: %ld\n", fileStats.st_size);
  printf("File Permissions: %o\n", fileStats.st_mode);
  bool isExecutable = fileStats.st_mode & S_IXUSR;
  printf("Executable: %s\n", isExecutable ? "true" : "false");
  char buffer[BUFFER_SIZE + 1];
  ssize_t bytesRead;
  while ((bytesRead = read(fd, buffer, BUFFER_SIZE))) {
    buffer[bytesRead] = '\0';
    printf("%s", buffer);
  }
}
