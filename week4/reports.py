#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, info):
    report = SimpleDocTemplate(file)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(info, styles['BodyText'])
    empty_line = Spacer(1,10)

    report.build([report_title, empty_line, report_info, empty_line])
