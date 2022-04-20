#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv[]){
  int fd;
  int i;
  if(argc < 2){
    fprintf(stderr, "USAGE: %s <filename>\n", argv[0]);
    exit(1);
  }
  for(i = 1; i < argc; i++){
    fd = open(argv[i], O_RDONLY);
    if(fd < 0){
      perror(argv[i]);
      continue;
    }
    printf("%s is opened as %d\n", argv[i], fd);
    close(fd);
  }
  return 0;
}
