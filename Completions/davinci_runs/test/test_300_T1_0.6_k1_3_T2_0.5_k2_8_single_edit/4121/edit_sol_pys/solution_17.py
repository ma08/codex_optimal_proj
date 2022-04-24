#include "file.h"

void read_file(char* file_name, char* buffer) {
    FILE* fp = fopen(file_name, "r");
    if(fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    fseek(fp, 0, SEEK_END);
    long fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    fread(buffer, fsize, 1, fp);
    fclose(fp);
}

void write_file(char* file_name, char* buffer) {
    FILE* fp = fopen(file_name, "w");
    if(fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    fwrite(buffer, sizeof(char), strlen(buffer), fp);
    fclose(fp);
}
