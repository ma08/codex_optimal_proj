

"""
This problem is a variant of Interval Scheduling problem.

Interval Scheduling problem is a problem of finding the maximum number of mutually compatible jobs. The jobs are specified by their start and finish times. Two jobs are compatible if they don't overlap.

This problem is solved by sorting the jobs by their finish times and then selecting the jobs greedily.

In this problem, we have to schedule $m$ exams and $n$ days. This can be done by creating $m$ jobs, where the start time of each job is the date when the questions are given and the end time is the date of the exam.

If the exam is passed in the same day when the questions are given, then the start and the end time of that job is the same.

The number of days required to prepare for the exam is not used in the solution.

We can sort the jobs by their end time and then select the jobs greedily. But it is not possible to select the jobs greedily in this problem.

For example, consider the following input.

4 2
1 4 2
2 3 1

The first job can be started in the first day and the second job can be started in the second day. So, the first job has to be completed in the third day, and the second job has to be completed in the fourth day.

But if the first job is completed in the third day, then the second job can not be completed in the fourth day because the first job ends in the third day and the second job starts in the third day.

So, we have to select the jobs in such a way that the jobs with earlier end times are selected first.

The jobs can be sorted by their end times in $O(m \log m)$ time.

The jobs can be selected in $O(m)$ time.

So, the overall time complexity of the solution is $O(m \log m)$.
"""

def main():
    n, m = map(int, input().split())
    jobs = []
    for _ in range(m):
        s, d, c = map(int, input().split())
        jobs.append((s, d, c))
    jobs.sort(key=lambda x: x[1])

    schedule = [0] * n
    for s, d, c in jobs:
        if not schedule[s - 1]:
            schedule[s - 1] = d
        else:
            for i in range(s, min(d, n)):
                if not schedule[i]:
                    schedule[i] = d
                    break
            else:
                print(-1)
                return

    for i, d in enumerate(schedule):
        if d:
            schedule[i] = d - i
    print(*schedule)

if __name__ == '__main__':
    main()