

num_survey = int(input())

survey_list = []
for i in range(num_survey):
    survey_list.append(list(map(int, input().split())))

survey_list.sort()

x = y = 0
for i in range(num_survey - 1):
    x += survey_list[i][0]
    y += survey_list[i][1]

x = round(x / (num_survey - 1))
y = round(y / (num_survey - 1))

h = 0
for i in range(num_survey):
    h = max(h, survey_list[i][2] + abs(survey_list[i][0] - x) + abs(survey_list[i][1] - y))

print("{} {} {}".format(x, y, h))