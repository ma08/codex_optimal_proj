#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    FILE *fp;
    char ch;
    int count = 0;

    fp = fopen("file.txt", "r");
    if (fp == NULL)
    {
        printf("File does not exist\n");
        exit(1);
    }

    while ((ch = fgetc(fp)) != EOF)
    {
        count++;
    }

    printf("Number of characters in file is %d\n", count);

    fclose(fp);
    return 0;
}
