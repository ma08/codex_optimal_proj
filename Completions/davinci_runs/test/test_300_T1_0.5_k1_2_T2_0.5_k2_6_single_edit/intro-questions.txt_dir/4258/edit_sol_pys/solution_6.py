#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LEN 8

int main(int argc, char *argv[])
{
    FILE *fp;
    char buf[LEN];
    int i;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        exit(1);
    }

    if ((fp = fopen(argv[1], "r")) == NULL)
    {
        fprintf(stderr, "Can't open %s\n", argv[1]);
        exit(1);
    }

    for (i = 0; i < LEN; i++)
        buf[i] = getc(fp);

    if (strncmp(buf, "\x7fELF", 4) == 0)
    {
        printf("%s is an ELF executable.\n", argv[1]);
        exit(0);
    }

    if (strncmp(buf, "MZ", 2) == 0)
    {
        printf("%s is an MS-DOS executable.\n", argv[1]);
        exit(0);
    }

    if (strncmp(buf, "\xFE\xED\xFA\xCE", 4) == 0)
    {
        printf("%s is a Mach-O executable.\n", argv[1]);
        exit(0);
    }

    printf("%s is an unknown executable.\n", argv[1]);
    exit(0);
}
