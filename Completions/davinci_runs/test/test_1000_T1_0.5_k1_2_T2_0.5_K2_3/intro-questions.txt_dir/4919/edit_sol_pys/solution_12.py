#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);
    int **trips = (int **)malloc(n * sizeof(int *));
    int *trip_counts = (int *)calloc(n, sizeof(int));
    char **trip_names = (char **)malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++) {
        char *country = (char *)malloc(101 * sizeof(char));
        int year;
        scanf("%s %d", country, &year);
        int j;
        for (j = 0; j < i; j++) {
            if (strcmp(trip_names[j], country) == 0) {
                break;
            }
        }
        if (j == i) {
            trip_names[j] = country;
            trips[j] = (int *)malloc(sizeof(int));
            trip_counts[j] = 1;
        } else {
            trips[j] = (int *)realloc(trips[j], (trip_counts[j] + 1) * sizeof(int));
            trip_counts[j]++;
        }
        trips[j][trip_counts[j] - 1] = year;
    }
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        char *country = (char *)malloc(101 * sizeof(char));
        int k;
        scanf("%s %d", country, &k);
        int j;
        for (j = 0; j < n; j++) {
            if (strcmp(trip_names[j], country) == 0) {
                break;
            }
        }
        printf("%d\n", trips[j][k - 1]);
    }
    for (int i = 0; i < n; i++) {
        free(trips[i]);
        free(trip_names[i]);
    }
    free(trips);
    free(trip_names);
    free(trip_counts);

    return 0;
}
