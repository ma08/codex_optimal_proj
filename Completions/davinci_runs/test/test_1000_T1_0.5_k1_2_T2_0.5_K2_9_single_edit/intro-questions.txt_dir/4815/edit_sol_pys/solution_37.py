#!/usr/bin/env python

import csv
import sys

from datetime import datetime
from datetime import timedelta

def parse_date(date):
    return datetime.strptime(date, '%Y-%m-%d')

def parse_time(time):
    return datetime.strptime(time, '%H:%M:%S').time()

def parse_datetime(datetime_string):
    date, time = datetime_string.split()
    return datetime.combine(parse_date(date), parse_time(time))

def parse_duration(duration_string):
    hours, minutes, seconds = duration_string.split(':')
    return timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

def parse_row(row):
    return {
        'id': int(row['id']),
        'start': parse_datetime(row['start']),
        'duration': parse_duration(row['duration']),
        'topic': row['topic'],
        'tutor': row['tutor'],
        'student': row['student']
    }

def read_data(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        return [parse_row(row) for row in reader]

def get_student_list(data):
    return list(set(row['student'] for row in data))

def get_tutor_list(data):
    return list(set(row['tutor'] for row in data))

def get_topic_list(data):
    return list(set(row['topic'] for row in data))

def get_student_hours(data, student):
    return sum(row['duration'] for row in data if row['student'] == student)

def get_tutor_hours(data, tutor):
    return sum(row['duration'] for row in data if row['tutor'] == tutor)

def get_topic_hours(data, topic):
    return sum(row['duration'] for row in data if row['topic'] == topic)

def get_student_topics(data, student):
    return [row['topic'] for row in data if row['student'] == student]

def get_tutor_topics(data, tutor):
    return [row['topic'] for row in data if row['tutor'] == tutor]

def get_student_tutors(data, student):
    return [row['tutor'] for row in data if row['student'] == student]

def get_tutor_students(data, tutor):
    return [row['student'] for row in data if row['tutor'] == tutor]

def get_topic_tutors(data, topic):
    return [row['tutor'] for row in data if row['topic'] == topic]

def get_topic_students(data, topic):
    return [row['student'] for row in data if row['topic'] == topic]

def get_topic_tutor_hours(data, topic, tutor):
    return sum(row['duration'] for row in data if row['topic'] == topic and row['tutor'] == tutor)

def get_tutor_topic_hours(data, tutor, topic):
    return sum(row['duration'] for row in data if row['tutor'] == tutor and row['topic'] == topic)

def get_tutor_student_hours(data, tutor, student):
    return sum(row['duration'] for row in data if row['tutor'] == tutor and row['student'] == student)

def get_student_tutor_hours(data, student, tutor):
    return sum(row['duration'] for row in data if row['student'] == student and row['tutor'] == tutor)

def get_topic_student_hours(data, topic, student):
    return sum(row['duration'] for row in data if row['topic'] == topic and row['student'] == student)

def get_student_topic_hours(data, student, topic):
    return sum(row['duration'] for row in data if row['student'] == student and row['topic'] == topic)

def get_tutor_hours_by_topic(data, tutor):
    return {topic: get_tutor_topic_hours(data, tutor, topic) for topic in get_topic_list(data)}

def get_topic_hours_by_tutor(data, topic):
    return {tutor: get_topic_tutor_hours(data, topic, tutor) for tutor in get_tutor_list(data)}

def get_student_hours_by_topic(data, student):
    return {topic: get_student_topic_hours(data, student, topic) for topic in get_topic_list(data)}

def get_topic_hours_by_student(data, topic):
    return {student: get_topic_student_hours(data, topic, student) for student in get_student_list(data)}

def get_student_hours_by_tutor(data, student):
    return {tutor: get_student_tutor_hours(data, student, tutor) for tutor in get_tutor_list(data)}

def get_tutor_hours_by_student(data, tutor):
    return {student: get_tutor_student_hours(data, tutor, student) for student in get_student_list(data)}

def get_tutor_hours_by_topic_by_student(data, tutor):
    return {student: get_tutor_hours_by_topic(data, tutor) for student in get_student_list(data)}

def main(argv):
    data = read_data(argv[1])

    print('Students: {}'.format(get_student_list(data)))
    print('Tutors: {}'.format(get_tutor_list(data)))
    print('Topics: {}'.format(get_topic_list(data)))

    print('Student Hours: {}'.format({student: get_student_hours(data, student) for student in get_student_list(data)}))
    print('Tutor Hours: {}'.format({tutor: get_tutor_hours(data, tutor) for tutor in get_tutor_list(data)}))
    print('Topic Hours: {}'.format({topic: get_topic_hours(data, topic) for topic in get_topic_list(data)}))

    print('Student Topics: {}'.format({student: get_student_topics(data, student) for student in get_student_list(data)}))
    print('Tutor Topics: {}'.format({tutor: get_tutor_topics(data, tutor) for tutor in get_tutor_list(data)}))

    print('Student Tutors: {}'.format({student: get_student_tutors(data, student) for student in get_student_list(data)}))
    print('Tutor Students: {}'.format({tutor: get_tutor_students(data, tutor) for tutor in get_tutor_list(data)}))

    print('Topic Tutors: {}'.format({topic: get_topic_tutors(data, topic) for topic in get_topic_list(data)}))
    print('Topic Students: {}'.format({topic: get_topic_students(data, topic) for topic in get_topic_list(data)}))

    print('Tutor Hours by Topic: {}'.format({tutor: get_tutor_hours_by_topic(data, tutor) for tutor in get_tutor_list(data)}))
    print('Topic Hours by Tutor: {}'.format({topic: get_topic_hours_by_tutor(data, topic) for topic in get_topic_list(data)}))

    print('Student Hours by Topic: {}'.format({student: get_student_hours_by_topic(data, student) for student in
