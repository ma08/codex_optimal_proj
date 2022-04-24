#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 1024

int main(int argc, char *argv[]){

	int i;
	char *s;
	FILE *fp;
	char buf[MAX_LENGTH];

	if(argc <2){
		fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
		exit(1);
	}

	for(i=1; i<argc; i++) {
		fp = fopen(argv[i], "r");
		if(fp == NULL){
			perror("fopen failed");
			exit(1);
		}

		while(fgets(buf, MAX_LENGTH, fp)){
			s = strtok(buf, " \t\n");
			while(s != NULL){
				printf("%s\n", s);
				s = strtok(NULL, " \t\n");
			}
		}
		fclose(fp);
	}
	return 0;
}
