#!/usr/bin/env python3
import email
import os
import reports

if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    pdf = reports.generate_pdf(path)
    reports.generate_report('/tmp/processed.pdf', "Updated on ", pdf)

    sender = "automation@example.com"
    receiver = "/home/student"
    subject = "Upload Successful"
    body = "All the items were uploaded to the website. (See attachment for more details)"
    attachment = "/tmp/processed.pdf"

    message = email.generate_email(sender, receiver, subject, body, attachment)
    email.send_email(message)


