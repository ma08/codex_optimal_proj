from datetime import datetime
from datetime import timedelta
import os


class File:
    def __init__(self, definition):
        self.definition = definition
        self.name = definition.get('name')
        self.path = definition.get('path')
        self.size = definition.get('size')
        self.date = definition.get('date')
        self.time = definition.get('time')
        self.type = definition.get('type')

    def __repr__(self):
        return f'<File {self.name}>'

    @property
    def full_path(self):
        return os.path.join(self.path, self.name)

    @property
    def date_time(self):
        return datetime.strptime(f'{self.date} {self.time}', '%m/%d/%Y %H:%M:%S')

    def is_older_than(self, days=0, hours=0, minutes=0, seconds=0):
        age = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return datetime.now() - age > self.date_time

    def is_newer_than(self, days=0, hours=0, minutes=0, seconds=0):
        age = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return datetime.now() - age < self.date_time

    def is_older_than_days(self, days):
        return self.is_older_than(days=days)

    def is_newer_than_days(self, days):
        return self.is_newer_than(days=days)

    def is_older_than_hours(self, hours):
        return self.is_older_than(hours=hours)

    def is_newer_than_hours(self, hours):
        return self.is_newer_than(hours=hours)

    def is_older_than_minutes(self, minutes):
        return self.is_older_than(minutes=minutes)

    def is_newer_than_minutes(self, minutes):
        return self.is_newer_than(minutes=minutes)

    def is_older_than_seconds(self, seconds):
        return self.is_older_than(seconds=seconds)

    def is_newer_than_seconds(self, seconds):
        return self.is_newer_than(seconds=seconds)

    def is_of_size(self, size):
        return size == self.size

    def is_of_type(self, type):
        return type == self.type

    def is_bigger_than(self, size):
        return size < self.size

    def is_smaller_than(self, size):
        return size > self.size

    def is_bigger_than_mb(self, size):
        return size < self.size

    def is_smaller_than_mb(self, size):
        return size > self.size

    def is_bigger_than_gb(self, size):
        return size * 1024 < self.size

    def is_smaller_than_gb(self, size):
        return size * 1024 > self.size

    def is_bigger_than_kb(self, size):
        return size / 1024 < self.size

    def is_smaller_than_kb(self, size):
        return size / 1024 > self.size

    def is_of_size_kb(self, size):
        return size / 1024 == self.size

    def is_of_size_mb(self, size):
        return size == self.size

    def is_of_size_gb(self, size):
        return size * 1024 == self.size

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size != 0
