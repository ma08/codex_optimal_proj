#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char fileName[20];
	char fileContent[100];
	char fileContent2[100];
	char fileContent3[100];

	printf("Enter file name\n");
	scanf("%s", &fileName);

	printf("Enter file content\n");
	scanf("%s", &fileContent);

	FILE *file;
	file = fopen(fileName, "w");
	fprintf(file, "%s", fileContent);
	fclose(file);

	file = fopen(fileName, "r");
	fscanf(file, "%s", &fileContent2);
	fclose(file);

	printf("%s\n", fileContent2);

	file = fopen(fileName, "a");
	fprintf(file, "%s", " and more");
	fclose(file);

	file = fopen(fileName, "r");
	fscanf(file, "%s", &fileContent3);
	fclose(file);

	printf("%s\n", fileContent3);

	return 0;
}
