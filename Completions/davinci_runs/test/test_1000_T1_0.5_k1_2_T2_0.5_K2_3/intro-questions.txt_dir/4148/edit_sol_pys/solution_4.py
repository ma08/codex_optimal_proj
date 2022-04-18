#include <stdio.h> //library for input and output

int main() {
    int n; //number of shift
    char s[101]; //string

    scanf("%d", &n); //input the number of shift
    scanf("%s", s); //input the string

    int i; //counter
    for(i = 0; s[i] != '\0'; i++) { //loop for each letter in the string
        if (s[i] + n > 'Z') { //if the letter is shifted over the alphabet
            printf("%c", s[i] + n - 26); //print the letter with the shift minus 26
        }
        else {
            printf("%c", s[i] + n);
        }
    }
}
