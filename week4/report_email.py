#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
from emails import generate_email , send_email

def pdf_body(input_for, desc_dir):
    res = []
    wt = []
    for item in os.listdir(desc_dir):
        filename = os.path.join(desc_dir, item)
        with open(filename) as f:
            line = f.readlines()
            weight=line[1].strip('\n')
            name = line[0].strip('\n')
            print(name, weight)
            res.append('name: '+ name)
            wt.append('weight: '+ weight)
            print(res, wt)
    new_obj = ""
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on {}'.format(str(current_date))
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf', description_directory))

    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    msg = generate_email("automation@example.com", user+'@example.com', email_subject, email_body, "/tmp/processed.pdf")
    send_email(msg)
