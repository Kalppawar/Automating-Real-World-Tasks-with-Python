#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails
import os

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_disk_usage(disk):
    # check if more than 20% disk space is available
    usage = shutil.disk_usage(disk)
    free = (usage.free/usage.total) * 100
    return free > 20

def check_memory_usage():
    usage = psutil.virtual_memory().available
    total = usage/(1024 ** 2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def send_simple_email(email_subject):
    user = os.getenv('USER')
    email_body = 'Please check your system and resolve the issue as soon as possible.'
    email_obj = emails.generate_email("automation@example.com", user+'@example.com', email_subject, email_body)
    emails.send_email(email_obj)


if not check_cpu_usage():
    subject = 'Error - CPU usage is over 80%'
    print(subject)
    send_simple_email(subject)

if not check_memory_usage():
    subject = 'Error - Available memory is less than 500MB'
    print(subject)
    send_simple_email(subject)

if not check_disk_usage('/'):
    subject = 'Error - Available disk space is less than 20%'
    print(subject)
    send_simple_email(subject)

if not check_localhost():
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    print(subject)
    send_simple_email(subject)
