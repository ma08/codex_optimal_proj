#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *str_replace(char *orig, char *rep, char *with) {
    char *result; // the return string
    char *ins;    // the next insert point
    char *tmp;    // varies
    int len_rep;  // length of rep (the string to remove)
    int len_with; // length of with (the string to replace rep with)
    int len_front; // distance between rep and end of last rep
    int count;    // number of replacements

    // sanity checks and initialization
    if (!orig || !rep)
        return NULL;
    len_rep = strlen(rep);
    if (len_rep == 0)
        return NULL; // empty rep causes infinite loop during count
    if (!with)
        with = "";
    len_with = strlen(with);

    // count the number of replacements needed
    ins = orig;
    for (count = 0; tmp = strstr(ins, rep); ++count) {
        ins = tmp + len_rep;
    }

    tmp = result = malloc(strlen(orig) + (len_with - len_rep) * count + 1);

    if (!result)
        return NULL;

    // first time through the loop, all the variable are set correctly
    // from here on,
    //    tmp points to the end of the result string
    //    ins points to the next occurrence of rep in orig
    //    orig points to the remainder of orig after "end of rep"
    while (count--) {
        ins = strstr(orig, rep);
        len_front = ins - orig;
        tmp = strncpy(tmp, orig, len_front) + len_front;
        tmp = strcpy(tmp, with) + len_with;
        orig += len_front + len_rep; // move to next "end of rep"
    }
    strcpy(tmp, orig);
    return result;
}

char *readFile(char *filename) {
    FILE *file = fopen(filename, "r");
    char *code;
    size_t n = 0;
    int c;

    if (file == NULL)
        return NULL; //could not open file

    fseek(file, 0, SEEK_END);
    long f_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    code = malloc(f_size);

    while ((c = fgetc(file)) != EOF) {
        code[n++] = (char) c;
    }

    code[n] = '\0';

    return code;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("no file specified\n");
        return 1;
    }

    char *code = readFile(argv[1]);
    if (code == NULL) {
        printf("could not read file\n");
        return 1;
    }

    code = str_replace(code, "()", "");
    code = str_replace(code, "++", "+");
    code = str_replace(code, "--", "-");

    char *p = code;

    int brackets = 0;
    int mem_pos = 0;
    unsigned char mem[30000] = {0};

    while (*p != '\0') {
        if (*p == '+') {
            mem[mem_pos]++;
        } else if (*p == '-') {
            mem[mem_pos]--;
        } else if (*p == '>') {
            mem_pos++;
        } else if (*p == '<') {
            mem_pos--;
        } else if (*p == '.') {
            putchar(mem[mem_pos]);
        } else if (*p == ',') {
            mem[mem_pos] = getchar();
        } else if (*p == '[') {
            if (mem[mem_pos] == 0) {
                brackets = 1;
                while (brackets > 0) {
                    p++;
                    if (*p == '[') {
                        brackets++;
                    } else if (*p == ']') {
                        brackets--;
                    }
                }
            }
        } else if (*p == ']') {
            if (mem[mem_pos] != 0) {
                brackets = 1;
                while (brackets > 0) {
                    p--;
                    if (*p == '[') {
                        brackets--;
                    } else if (*p == ']') {
                        brackets++;
                    }
                }
            }
        }
        p++;
    }

    free(code);
    return 0;
}
