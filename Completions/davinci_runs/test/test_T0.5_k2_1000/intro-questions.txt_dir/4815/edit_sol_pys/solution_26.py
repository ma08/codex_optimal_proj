#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>

#define PORT 8080
#define BUFSIZE 1024

int main(int argc, char *argv[])
{
    int sockfd;
    struct sockaddr_in servaddr;
    char sendline[BUFSIZE], recvline[BUFSIZE];

    if (argc != 2) {
        printf("usage: %s <IPaddress>\n", argv[0]);
        exit(1);
    }

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("create socket error: %s(errno: %d)\n", strerror(errno), errno);
        exit(1);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0) {
        printf("inet_pton error for %s\n", argv[1]);
        exit(1);
    }

    if (connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0) {
        printf("connect error: %s(errno: %d)\n", strerror(errno), errno);
        exit(1);
    }

    printf("send msg to server: \n");
    fgets(sendline, BUFSIZE, stdin);
    if (send(sockfd, sendline, strlen(sendline), 0) < 0) {
        printf("send msg error: %s(errno: %d)\n", strerror(errno), errno);
        exit(1);
    }

    close(sockfd);
    exit(0);
}
