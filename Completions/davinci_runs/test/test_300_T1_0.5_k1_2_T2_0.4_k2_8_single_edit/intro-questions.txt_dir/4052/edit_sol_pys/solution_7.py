#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);
    return 1;
  }

  FILE *f = fopen(argv[1], "r");
  if (f == NULL) {
    printf("Error opening file %s\n", argv[1]);
    return 1;
  }

  char line[1024];
  while (fgets(line, 1024, f)) {
    char *token = strtok(line, " ");
    while (token) {
      printf("%s\n", token);
      token = strtok(NULL, " ");
    }
  }

  fclose(f);

  return 0;
}
