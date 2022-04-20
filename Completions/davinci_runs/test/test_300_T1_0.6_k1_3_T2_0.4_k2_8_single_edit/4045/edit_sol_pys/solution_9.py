#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LENGTH 256

int main(int argc, char *argv[]) {
    FILE *fp;
    char str[MAX_STRING_LENGTH];
    char *filename;
    char *search_str;
    char *replace_str;
    int line_number = 1;
    int find_result = 0;

    if (argc < 4) {
        printf("Usage: %s [FILE] [SEARCH_STRING] [REPLACE_STRING]\n", argv[0]);
        return 1;
    }
    filename = argv[1];
    search_str = argv[2];
    replace_str = argv[3];

    if ((fp = fopen(filename, "r")) == NULL) {
        printf("Cannot open file %s\n", filename);
        return 1;
    }
    while (fgets(str, MAX_STRING_LENGTH, fp) != NULL) {
        if ((strstr(str, search_str)) != NULL) {
            printf("A match found on line: %d\n", line_number);
            printf("\n%s\n", str);
            find_result++;
        }
        line_number++;
    }

    if (find_result == 0) {
        printf("\nSorry, couldn't find a match.\n");
    }

    // Close the file if still open.
    if (fp) {
        fclose(fp);
    }

    return 0;
}
