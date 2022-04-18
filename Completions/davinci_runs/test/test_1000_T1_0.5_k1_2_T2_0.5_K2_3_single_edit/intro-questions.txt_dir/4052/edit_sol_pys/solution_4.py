#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include <fcntl.h>
#include <sys/stat.h>

#define BUFFER_SIZE 25
#define READ_END 0
#define WRITE_END 1
#define SHM_SIZE 1024

int main()
{
    int fd[2];
    pid_t pid;
    char write_msg[BUFFER_SIZE] = "Greetings";
    char read_msg[BUFFER_SIZE];
    int shm_id;
    int *shm_ptr;
    key_t key;

    key = ftok("/tmp", 'a');
    shm_id = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    shm_ptr = shmat(shm_id, NULL, 0);

    if (pipe(fd) == -1)
    {
        fprintf(stderr, "Pipe failed");
        return 1;
    }

    pid = fork();

    if (pid < 0)
    {
        fprintf(stderr, "Fork failed");
        return 1;
    }

    if (pid > 0)
    {
        close(fd[READ_END]);
        write(fd[WRITE_END], write_msg, strlen(write_msg) + 1);
        close(fd[WRITE_END]);
        wait(NULL);
        printf("Child wrote: [%s]\n", shm_ptr);
    }
    else
    {
        close(fd[WRITE_END]);
        read(fd[READ_END], read_msg, BUFFER_SIZE);
        close(fd[READ_END]);
        sprintf(shm_ptr, "Child read: [%s]\n", read_msg);
    }

    shmdt(shm_ptr);
    shmctl(shm_id, IPC_RMID, NULL);

    return 0;
}
