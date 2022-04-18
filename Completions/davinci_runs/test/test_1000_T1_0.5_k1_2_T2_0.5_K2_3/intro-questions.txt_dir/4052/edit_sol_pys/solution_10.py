#include<stdio.h>

int main(void)
{
    int c;
    FILE *fp;

    fp = fopen("/home/naz/Desktop/C/file.txt", "r");
    if(fp == NULL)
        perror("Error opening file");
    else
    {
        while((c = getc(fp)) != EOF)
            putchar(c);
        fclose(fp);
    }

    return 0;
}
