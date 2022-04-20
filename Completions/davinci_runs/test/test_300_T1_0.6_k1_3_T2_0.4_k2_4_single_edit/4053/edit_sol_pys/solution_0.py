#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>

#define MAX_ARGS 64
#define MAX_ARG_LEN 16
#define MAX_LINE_LEN 512
#define WHITESPACE " .,\t\n"

struct command_t {
  char *name;
  int argc;
  char *argv[MAX_ARGS];
};

/* Function prototypes */
int parseCommand(char *, struct command_t *);
void printPrompt();
void readCommand(char *);

int main() {
  char *cmdLine;
  struct command_t command;
  int pid, status;
  int i;
  int fd;

  cmdLine = (char *) malloc(MAX_LINE_LEN);

  while (1) {
    printPrompt();
    /* Read the command line and parse it */
    readCommand(cmdLine);
    //printf("DEBUG: Command entered: %s\n", cmdLine);

    parseCommand(cmdLine, &command);

    /* Create a child process to execute the command */
    pid = fork();

    if (pid < 0) {
      /* Error occurred */
      fprintf(stderr, "Fork failed\n");
      exit(1);
    }
    else if (pid == 0) {
      /* Child process */
      if (strcmp(command.argv[command.argc - 1], "&") == 0) {
        command.argv[command.argc - 1] = NULL;
        command.argc--;
      }

      for (i = 0; i < command.argc; i++) {
        if (strcmp(command.argv[i], ">") == 0) {
          fd = open(command.argv[i + 1], O_WRONLY | O_CREAT, 0644);
          dup2(fd, 1);
          close(fd);
          command.argv[i] = NULL;
        }
        else if (strcmp(command.argv[i], "<") == 0) {
          fd = open(command.argv[i + 1], O_RDONLY);
          dup2(fd, 0);
          close(fd);
          command.argv[i] = NULL;
        }
      }

      /* Execute the command */
      execvp(command.argv[0], command.argv);
    }
    else {
      /* Parent process */
      if (strcmp(command.argv[command.argc - 1], "&") == 0) {
        waitpid(pid, &status, WNOHANG);
      }
      else {
        waitpid(pid, &status, 0);
      }
    }
  }

  return 0;
}

/* End main */

/* Parse Command line and populate struct command_t */
int parseCommand(char *cLine, struct command_t *cmd) {
  int argc;
  char **clPtr;
  /* Initialization */
  clPtr = &cLine; /* cLine is the command line */
  argc = 0;
  cmd->argv[argc] = (char *) malloc(MAX_ARG_LEN);
  /* Fill argv[] */
  while ((cmd->argv[argc] = strsep(clPtr, WHITESPACE)) != NULL) {
    cmd->argv[++argc] = (char *) malloc(MAX_ARG_LEN);
  }

  /* Set the command name and argc */
  cmd->argc = argc - 1;
  cmd->name = (char *) malloc(sizeof(cmd->argv[0]));
  strcpy(cmd->name, cmd->argv[0]);
  return 1;
}

/* Print prompt and read command functions - pp. 79-80 */
void printPrompt() {
  printf("myshell>");
}

void readCommand(char *buffer) {
  fgets(buffer, MAX_LINE_LEN, stdin);
}
