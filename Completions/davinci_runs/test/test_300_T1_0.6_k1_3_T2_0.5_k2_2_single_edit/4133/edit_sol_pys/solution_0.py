#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fp;
    char *str = "Hello World!";
    char buff[1024];

    fp = fopen("file.txt", "w+");
    fwrite(str, 1, strlen(str), fp);
    rewind(fp);
    fread(buff, 1, sizeof(buff), fp);
    printf("%s\n", buff);
    fclose(fp);

    return 0;
}
