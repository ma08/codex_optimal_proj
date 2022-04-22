#include <stdio.h>

int main(int argc, char* argv[])
{
  FILE *fp;
  fp = fopen(argv[1], "r");
  if(fp == NULL)
  {
    perror("File opening failed");
    return -1;
  }
  char c = fgetc(fp);
  while(c != EOF)
  {
    putchar(c);
    c = fgetc(fp);
  }
  fclose(fp);
  return 0;
}
