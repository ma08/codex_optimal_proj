#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *file;
    file = fopen("file.txt", "w");
    if(file == NULL)
    {
        printf("Error");
        exit(1);
    }
    fprintf(file, "Hello World!");
    fclose(file);
    
    return 0;
}
