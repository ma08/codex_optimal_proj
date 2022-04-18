
N = int(input())
events = []

for i in range(N):
    event = tuple(map(int, input().split()))
    events.append(event)
# sort events by start time
events = sorted(events, key=lambda e: e[0])
# initialize the last event to be the first event
last_event = events[0]
# initialize the number of days with free food to the duration of the first event
days_with_free_food = last_event[1] - last_event[0] + 1
for event in events:
    if event[0] <= last_event[1]:
        # if the current event starts before the last event ends
        # then the current event overlaps the last event
        # if the current event ends after the last event ends, then we need to add the difference to days_with_free_food
        if event[1] > last_event[1]:
            days_with_free_food += event[1] - last_event[1]
    else:
        # if the current event doesn't overlap the last event, then we need to add the duration of the current event to days_with_free_food
        days_with_free_food += event[1] - event[0] + 1
    last_event = event

print(days_with_free_food)
