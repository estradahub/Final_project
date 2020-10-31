#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os


date = datetime.datetime.today()
def generate_pdf(path):
    formated_body = ""
    files = os.listdir(path)    
    for file in files:
        with open(path+file, 'r') as f:
            content = f.readlines()
            name = content[0].strip()
            weight = content[1].strip()
            formated_body += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return formated_body

title = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
report = SimpleDocTemplate('/home/bryan/Documents/report_lab.pdf')
styles = getSampleStyleSheet()
report_title = Paragraph("Updated on {}".format(title), styles["h1"])  
info = generate_pdf('/home/bryan/Documents/text_files/')
report_info = Paragraph(info, styles['BodyText'])
space = Spacer(1,20)
report.build([report_title, space, report_info, space])

