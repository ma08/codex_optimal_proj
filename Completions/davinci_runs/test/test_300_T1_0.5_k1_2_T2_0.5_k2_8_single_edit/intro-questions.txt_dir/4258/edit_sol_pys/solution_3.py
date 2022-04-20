#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "A-large-practice.in"

int main()
{
	FILE *fp = fopen(FILENAME, "r");
	FILE *fp_out = fopen("output.txt","w");
	int t, n, s, p, i, j, k, score, num_surprise, num_pass;
	int *scores;
	fscanf(fp, "%d", &t);
	for(i=0; i<t; i++)
	{
		fscanf(fp, "%d %d %d", &n, &s, &p);
		scores = (int *)malloc(sizeof(int)*n);
		for(j=0; j<n; j++)
		{
			fscanf(fp, "%d", &scores[j]);
		}
		num_pass = 0;
		num_surprise = 0;
		for(j=0; j<n; j++)
		{
			score = scores[j];
			if(score % 3 == 0)
			{
				if(score/3 >= p)
				{
					num_pass++;
				}
				else if(score/3 >= p-1 && score/3 > 0 && s > 0)
				{
					num_pass++;
					num_surprise++;
				}
			}
			else if(score % 3 == 1)
			{
				if(score/3 + 1 >= p)
				{
					num_pass++;
				}
			}
			else
			{
				if(score/3 + 1 >= p)
				{
					num_pass++;
				}
				else if(score/3 + 2 >= p && s > 0)
				{
					num_pass++;
					num_surprise++;
				}
			}
		}
		fprintf(fp_out, "Case #%d: %d\n", i+1, num_pass);
	}
	fclose(fp);
	fclose(fp_out);
	return 0;
}
