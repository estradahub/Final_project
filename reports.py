#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os



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

def generate_report(file, title, info):
    date = datetime.date.today().strftime("%B %d, %Y") 
    report = SimpleDocTemplate('/where to put the pdf/name(processed.pdf)')
    styles = getSampleStyleSheet()
    report_title = Paragraph("{} {}".format(title,date), styles["h1"])  
    info = generate_pdf('/where the text files are located/')
    report_info = Paragraph(info, styles['BodyText'])
    space = Spacer(1,20)
    report.build([report_title, space, report_info, space])

