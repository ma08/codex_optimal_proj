#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;
    int i;
    if (argc != 2)
    {
        printf("Usage: %s filename\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    if ((fp = fopen(argv[1], "r")) == NULL)
    {
        printf("Can't open %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }
    i = 0;
    while ((ch = getc(fp)) != EOF)
    {
        putc(ch, stdout);
        i++;
    }
    fclose(fp);
    printf("\n%s has %d characters\n", argv[1], i);

    return 0;
}
