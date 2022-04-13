#include<stdio.h>

int main(void)
{
    FILE *fp = NULL;

    fp = fopen("/home/naz/Desktop/C/file.txt", "w");
    fprintf(fp, "This is testing for fprintf...\n");
    fputs("This is testing for fputs...\n", fp);
    fclose(fp);

    return 0;
}
