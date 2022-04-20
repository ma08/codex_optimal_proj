from collections import defaultdict


def max_overlap(n, start_times, end_times):
    # create a dictionary of start times
    start_times_dict = defaultdict(int)
    for time in start_times:
        start_times_dict[time] += 1
    # create a dictionary of end times
    end_times_dict = defaultdict(int)
    for time in end_times:
        end_times_dict[time] += 1
    # create a dictionary of times
    times_dict = defaultdict(int)
    for time in start_times + end_times:
        times_dict[time] += 1
    # create a list of times
    times = list(times_dict.keys())
    times.sort()
    # create a list of overlap counts
    overlap_counts = [0]
    for time in times:
        overlap_counts.append(overlap_counts[-1] + start_times_dict[time] - end_times_dict[time])
    # return the max overlap count
    return max(overlap_counts)

n = int(input()) # number of meetings
start_times = []
end_times = []
for i in range(n):
    start_time, end_time = map(int, input().split()) # start and end times of the ith meeting
    start_times.append(start_time)
    end_times.append(end_time)

print(max_overlap(n, start_times, end_times))
