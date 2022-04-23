#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("ERROR: You need at least one argument.\n");
        // this is how you abort a program
        return 1;
    }

    int i = 0;
    for (i = 0; i < argc; i++) {
        printf("arg %d: %s\n", i, argv[i]);
    }

    // Let's make our own array of strings
    char *states[] = {
        "California", "Oregon",
        "Washington", "Texas"
    };

    int num_states = 4;

    for (i = 0; i < num_states; i++) {
        printf("state %d: %s\n", i, states[i]);
    }

    return 0;
}
