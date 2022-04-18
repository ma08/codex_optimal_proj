#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

  FILE *infile, *outfile;
  char *input_file, *output_file;

  input_file = "input.txt";
  output_file = "output.txt";

  infile = fopen(input_file, "r");
  outfile = fopen(output_file, "w");

  char line[1024];
  char *token;
  int i, j, k;
  int sum;

  while (fgets(line, 1024, infile) != NULL){
    i = 0;
    j = 0;
    k = 0;
    sum = 0;

    token = strtok(line, " ");
    i = atoi(token);

    token = strtok(NULL, " ");
    j = atoi(token);

    token = strtok(NULL, " ");
    k = atoi(token);

    sum = i + j + k;
    fprintf(outfile, "%d\n", sum);
  }

  fclose(infile);
  fclose(outfile);

  return 0;
}
