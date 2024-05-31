#!/usr/bin/env python
import os
from datetime import datetime
from datetime import timedelta
from random import randint
from subprocess import Popen
import sys


def run(commands):
    Popen(commands).wait()

def message(date):
    return date.strftime('Worked on the main blog: %Y-%m-%d %H:%M')

def contributions_per_day(max_commits):
    max_c = max_commits
    if max_c > 20:
        max_c = 20
    if max_c < 1:
        max_c = 1
    return randint(1, max_c)

def contribute(date, file_name='assets/tests/worklog/TIMETRACK.md'):
    with open(os.path.join(os.getcwd(), file_name), 'a') as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def main_simple():
    curr_date = datetime.now()
    no_weekends = True
    frequency = 80
    days_before = 365
    days_after = 0
    max_commits = 10
    start_date = curr_date.replace(hour=20, minute=0) - timedelta(days_before)
    for day in (start_date + timedelta(n) for n
                in range(days_before + days_after)):
        if (not no_weekends or day.weekday() < 5) \
                and randint(0, 100) < frequency:
            for commit_time in (day + timedelta(minutes=m)
                                for m in range(contributions_per_day(max_commits))):
                contribute(commit_time)


if __name__ == "__main__":
    main_simple()