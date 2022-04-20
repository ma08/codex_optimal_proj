#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <time.h>
#include <errno.h>
#include <pwd.h>
#include <grp.h>
#include <fcntl.h>

void printFileInfo(struct stat *fileStat, char *fileName)
{
	char *time;
	char *fileType;

	if(S_ISREG(fileStat->st_mode))
		fileType = "Regular File";
	else if(S_ISDIR(fileStat->st_mode))
		fileType = "Directory";
	else if(S_ISCHR(fileStat->st_mode))
		fileType = "Character Device";
	else if(S_ISBLK(fileStat->st_mode))
		fileType = "Block Device";
	else if(S_ISFIFO(fileStat->st_mode))
		fileType = "FIFO";
	else if(S_ISLNK(fileStat->st_mode))
		fileType = "Link";
	else if(S_ISSOCK(fileStat->st_mode))
		fileType = "Socket";

	time = ctime(&fileStat->st_mtime);
	time[strlen(time) - 1] = '\0';

	printf("File Name: %s\n", fileName);
	printf("File Type: %s\n", fileType);
	printf("File Size: %d\n", fileStat->st_size);
	printf("File Permissions: %o\n", fileStat->st_mode);
	printf("File Owner: %s\n", getpwuid(fileStat->st_uid)->pw_name);
	printf("File Group: %s\n", getgrgid(fileStat->st_gid)->gr_name);
	printf("File Last Modified: %s\n", time);
}

int main(int argc, char *argv[])
{
	struct stat fileStat;
	int fd;
	char *fileName;
	char *fileContent;
	int fileSize;

	if(argc != 2)
	{
		printf("Usage: ./file <fileName>\n");
		exit(1);
	}

	fileName = argv[1];

	if(lstat(fileName, &fileStat) < 0)
	{
		printf("Error: %s\n", strerror(errno));
		exit(1);
	}

	printFileInfo(&fileStat, fileName);

	if(S_ISREG(fileStat.st_mode))
	{
		fileSize = fileStat.st_size;
		fileContent = (char *)malloc(fileSize);

		if((fd = open(fileName, O_RDONLY)) < 0)
		{
			printf("Error: %s\n", strerror(errno));
			exit(1);
		}

		if(read(fd, fileContent, fileSize) < 0)
		{
			printf("Error: %s\n", strerror(errno));
			exit(1);
		}

		printf("File Content:\n%s\n", fileContent);

		free(fileContent);
		close(fd);
	}

	return 0;
}
