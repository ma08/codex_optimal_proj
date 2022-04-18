#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <dirent.h>
#include <errno.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <directory>\n", argv[0]);
        exit(0);
    }

    DIR *dir = opendir(argv[1]);
    if (dir == NULL) {
        printf("Error: %s\n", strerror(errno));
        exit(0);
    }

    struct dirent *direntry = readdir(dir);
    struct stat statbuf;
    struct passwd *pwd;
    struct group *grp;
    struct tm *time;
    char date[100];

    while (direntry != NULL) {
        printf("%s\n", direntry->d_name);
        lstat(direntry->d_name, &statbuf);

        pwd = getpwuid(statbuf.st_uid);
        grp = getgrgid(statbuf.st_gid);
        time = localtime(&statbuf.st_mtime);
        strftime(date, 100, "%b %d %R", time);

        printf("  Owner: %s\n", pwd->pw_name);
        printf("  Group: %s\n", grp->gr_name);
        printf("  Size: %d\n", (int) statbuf.st_size);
        printf("  Permissions: %o\n", (unsigned int) statbuf.st_mode);
        printf("  Last Modified: %s\n", date);
        printf("\n");

        direntry = readdir(dir);
    }

    return 0;
}
