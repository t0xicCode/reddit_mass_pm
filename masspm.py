#!/usr/bin/env python
from __future__ import print_function

__author__ = 'xav0989'

import getpass

import praw


def print_space():
    print()
    print()


user_agent = 'Reddit Mass PM v0.1 by /u/xav0989'
p = praw.Reddit(user_agent=user_agent)

print('Welcome to Reddit Mass PM')

username = password = ''

while username == '' or password == '':
    username = raw_input('Who would you like to be today? ').strip()
    password = getpass.getpass('Password: ')

p.login(username=username, password=password)

if not p.is_logged_in():
    print('Login failed')
    exit(1)

print('Successful login')

print_space()

subject = raw_input('Title: ').strip()

print('Type EOF to finish the message entry')
print('Message: ')
content = ''
while True:
    input_str = raw_input('>')
    if input_str == 'EOF':
        break
    else:
        content = "\n".join([content, input_str])

print('Use commas to separate multiple recipients')
recipients = raw_input('Recipients: ').strip().split(',')

for recipient in recipients:
    p.send_message(recipient=recipient,subject=subject,message=content)