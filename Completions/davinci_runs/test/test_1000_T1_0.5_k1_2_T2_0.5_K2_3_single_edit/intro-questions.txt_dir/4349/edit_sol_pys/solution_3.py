#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_file(FILE *fp)
{
    int ch;
    while ((ch = fgetc(fp)) != EOF)
    {
        putchar(ch);
    }
}

int main(int argc, char *argv[])
{
    char *fname = argv[1];
    FILE *fp;

    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        exit(1);
    }

    fp = fopen(fname, "r");
    if (fp == NULL)
    {
        printf("%s cannot be opened\n", fname);
        exit(1);
    }

    print_file(fp);
    fclose(fp);

    return 0;
}
