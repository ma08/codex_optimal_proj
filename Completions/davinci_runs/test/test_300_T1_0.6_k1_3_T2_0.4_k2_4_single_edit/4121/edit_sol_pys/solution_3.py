#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
  int fd;
  char buf[1024];
  ssize_t nread;
  int i;

  if (argc < 2) {
    fprintf(stderr, "Usage: %s file...\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  for (i = 1; i < argc; i++) {
    fd = open(argv[i], O_RDONLY);
    if (fd == -1) {
      perror("open");
      continue;
    }

    while ((nread = read(fd, buf, sizeof(buf))) > 0)
      if (write(STDOUT_FILENO, buf, nread) != nread) {
        perror("write");
        exit(EXIT_FAILURE);
      }

    if (nread == -1) {
      perror("read");
      exit(EXIT_FAILURE);
    }

    if (close(fd) == -1) {
      perror("close");
      exit(EXIT_FAILURE);
    }
  }

  exit(EXIT_SUCCESS);
}
