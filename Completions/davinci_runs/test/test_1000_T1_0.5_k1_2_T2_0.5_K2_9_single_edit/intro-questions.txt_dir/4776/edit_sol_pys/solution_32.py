

N = int(input())

events = []

for i in range(N):
    event = tuple(map(int, input().split()))
    events.append(event)


events = sorted(events, key=lambda e: e[0])


last_event = events[0]


days_with_free_food = last_event[1] - last_event[0] + 1

for event in events:
    if event[0] <= last_event[1]:

        if event[1] > last_event[1]:
            days_with_free_food += event[1] - last_event[1]
    else:

        days_with_free_food += event[1] - event[0] + 1
    last_event = event

print(days_with_free_food)
