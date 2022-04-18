#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    char name[20];
    int age;
    float height;

    if((fp = fopen("data.txt", "r")) == NULL)
    {
        printf("\nCannot open file.\n");
        exit(1);
    }

    fscanf(fp, "%s %d %f", name, &age, &height);
    printf("%s %d %f", name, age, height);

    fclose(fp);

    return 0;
}
