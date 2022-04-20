#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fptr;
    int i, n, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10;
    int sum = 0;
    float avg = 0;
    char ch;
    char *filename = "file.txt";

    fptr = fopen(filename, "w");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    printf("Enter the number of integers to be written to the file: ");
    scanf("%d", &n);

    printf("Enter %d integers: ", n);

    for (i = 0; i < n; ++i) {
        scanf("%d", &n1);
        fprintf(fptr, "%d\n", n1);
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    while ((ch = fgetc(fptr)) != EOF) {
        printf("%c", ch);
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n2);
        sum += n2;
    }

    avg = (float)sum / n;

    printf("\nSum of all integers = %d\n", sum);
    printf("Average of all integers = %.2f", avg);

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n3);
        if (n3 % 2 == 0) {
            printf("\n%d is an even integer", n3);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n4);
        if (n4 % 2 != 0) {
            printf("\n%d is an odd integer", n4);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n5);
        if (n5 > 0) {
            printf("\n%d is a positive integer", n5);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n6);
        if (n6 < 0) {
            printf("\n%d is a negative integer", n6);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n7);
        if (n7 % 2 == 0 && n7 > 0) {
            printf("\n%d is an even positive integer", n7);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n8);
        if (n8 % 2 == 0 && n8 < 0) {
            printf("\n%d is an even negative integer", n8);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n9);
        if (n9 % 2 != 0 && n9 > 0) {
            printf("\n%d is an odd positive integer", n9);
        }
    }

    fclose(fptr);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }

    for (i = 0; i < n; ++i) {
        fscanf(fptr, "%d", &n10);
        if (n10 % 2 != 0 && n10 < 0) {
            printf("\n%d is an odd negative integer", n10);
        }
    }

    fclose(fptr);

    return 0;
}
