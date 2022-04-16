#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int n;
    int num;

    fp = fopen("test.txt", "r");
    if (fp == NULL) {
        printf("ファイルを開けませんでした。\n");
        exit(1);
    }

    while (fscanf(fp, "%d", &num) != EOF) {
        printf("%d\n", num);
    }

    fclose(fp);

    return 0;
}
