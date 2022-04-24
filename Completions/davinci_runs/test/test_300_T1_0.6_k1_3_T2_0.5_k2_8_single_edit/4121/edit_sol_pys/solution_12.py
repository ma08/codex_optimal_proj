#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>


int main(int argc, char** argv) {

  // check if the number of arguments is correct
  if (argc != 2) {
    printf("Wrong number of arguments\n");
    return -1;
  }
  
  // open the file
  FILE* fd = fopen(argv[1], "r");
  
  // check if the file exists
  if (fd == NULL) {
    printf("File does not exist\n");
    return -1;
  }
  
  // check if the file is empty
  if (fseek(fd, 0, SEEK_END) == 0) {
    printf("File is empty\n");
    return -1;
  }
  
  // get the size of the file
  fseek(fd, 0, SEEK_END);
  size_t file_size = ftell(fd);
  rewind(fd);
  
  // allocate memory for the buffer
  char* buffer = malloc(file_size * sizeof(char));
  
  // read the file
  size_t result = fread(buffer, sizeof(char), file_size, fd);
  
  // check if the file was read correctly
  if (result != file_size) {
    printf("Error reading the file\n");
    return -1;
  }
  
  // print the content of the file
  printf("%s", buffer);
  
  // close the file
  fclose(fd);
  
  return 0;
}
