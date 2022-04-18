#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {

    FILE *fp;
    int i;
    int num;
    int fsize = 1024;
    char *fname = "test.txt";

    fp = fopen(fname, "w+");
    if (fp == NULL) {
        printf("error: failed to open file\n");
        return -1;
    }

    srand(time(NULL));
    for (i = 0; i < fsize; i++) {
        num = rand() % 26 + 97;
        fputc(num, fp);
    }

    fclose(fp);

    return 0;
}
