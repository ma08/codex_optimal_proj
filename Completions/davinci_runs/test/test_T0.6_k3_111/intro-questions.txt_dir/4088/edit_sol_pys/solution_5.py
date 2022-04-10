#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_LENGTH 100

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    printf("Usage: %s <filename>\n", argv[0]);
    return 1;
  }

  FILE *file = fopen(argv[1], "r");
  if (file == NULL)
  {
    printf("Error: File not found\n");
    return 1;
  }

  char line[MAX_LENGTH];
  while (fgets(line, MAX_LENGTH, file))
  {
    size_t length = strlen(line);
    if (line[length - 1] == '\n')
    {
      line[length - 1] = '\0';
    }

    size_t i = 0;
    while (line[i] != '\0')
    {
      if (isalpha(line[i]))
      {
        if (isupper(line[i]))
        {
          line[i] = tolower(line[i]);
        }
        else
        {
          line[i] = toupper(line[i]);
        }
      }
      i++;
    }

    printf("%s\n", line);
  }

  fclose(file);
  return 0;
}
