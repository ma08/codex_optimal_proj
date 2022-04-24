
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/utsname.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include "header.h"
void check_env(char *input, char **env)
{
	int i = 0, j = 0, k = 0, len = strlen(input), flag = 0;
	char *name = (char *)malloc(sizeof(char) * len);
	while (input[i] != '=')
		name[i] = input[i++];
	i++;
	while (input[i] != '\0')
		name[i - 1] = input[i++];
	name[i - 1] = '\0';
	char *value = (char *)malloc(sizeof(char) * len);
	while (env[j] != NULL)
	{
		k = 0;
		while (env[j][k] != '=')
			k++;
		if (strncmp(name, env[j], k) == 0)
		{
			k++;
			while (env[j][k] != '\0')
				value[k - 1] = env[j][k++];
			printf("%s\n", value);
			flag = 1;
			break;
		}
		j++;
	}
	if (flag == 0)
	{
		printf("Variable not found\n");
	}
}
