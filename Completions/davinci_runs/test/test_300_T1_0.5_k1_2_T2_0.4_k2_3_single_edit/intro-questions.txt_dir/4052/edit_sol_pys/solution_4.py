#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){

  int fd;
  int pid;
  int status;
  int length;
  char *addr;
  char *filename;
  struct stat file_stat;

  if(argc != 2){
    printf("Usage: ./file <filename>\n");
    exit(1);
  }

  filename = argv[1];

  if(stat(filename, &file_stat) < 0){
    printf("Error: stat\n");
    exit(1);
  }

  length = file_stat.st_size;

  if((fd = open(filename, O_RDONLY)) < 0){
    printf("Error: open\n");
    exit(1);
  }

  if((addr = mmap(NULL, length, PROT_READ, MAP_PRIVATE, fd, 0)) == MAP_FAILED){
    printf("Error: mmap\n");
    exit(1);
  }

  if((pid = fork()) < 0){
    printf("Error: fork\n");
    exit(1);
  }

  if(pid == 0){
    int fd;
    char *temp;
    char *filename = "test.txt";

    if((fd = open(filename, O_RDWR | O_CREAT | O_TRUNC, 0600)) < 0){
      printf("Error: open\n");
      exit(1);
    }

    if(write(fd, addr, length) < 0){
      printf("Error: write\n");
      exit(1);
    }

    if(lseek(fd, 0, SEEK_SET) < 0){
      printf("Error: lseek\n");
      exit(1);
    }

    if((temp = mmap(NULL, length, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0)) == MAP_FAILED){
      printf("Error: mmap\n");
      exit(1);
    }

    for(int i = 0; i < length; i++){
      temp[i] = toupper(temp[i]);
    }

    if(munmap(temp, length) < 0){
      printf("Error: munmap\n");
      exit(1);
    }

    if(close(fd) < 0){
      printf("Error: close\n");
      exit(1);
    }

    exit(0);
  }

  if(wait(&status) < 0){
    printf("Error: wait\n");
    exit(1);
  }

  if(WIFEXITED(status) == 0){
    printf("Error: WIFEXITED\n");
    exit(1);
  }

  if(munmap(addr, length) < 0){
    printf("Error: munmap\n");
    exit(1);
  }

  if(close(fd) < 0){
    printf("Error: close\n");
    exit(1);
  }

  return 0;
}
