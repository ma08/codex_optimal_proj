#include <stdio.h>

int main()
{
    FILE *fp; // pointer to file

    fp = fopen("/home/naz/Desktop/C/file.txt", "w+"); // open file
    fprintf(fp, "This is testing for fprintf...\n"); // write string to file
    fputs("This is testing for fputs...\n", fp); // write string to file
    fclose(fp); // close file

    return 0;
}
