import smtplib
from os.path import basename
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, html="", files=None, server="127.0.0.1"):
	assert isinstance(send_to, list)
	msg = MIMEMultipart('alternative')
	msg['From'] = send_from
	msg['To'] =', '.join(send_to) 
	msg['Date'] = formatdate(localtime=True) 
	msg['Subject'] = subject
	msg.attach(MIMEText(text, 'plain'))
	if not html=="":
		msg.attach(MIMEText(html, 'html'))

	for f in files or []:
		with open (f, "rb") as attachment:
			part = MIMEBase ("application","octet-stream")
			part.set_payload(attachment.read()) 
		encoders.encode_base64(part)
		part.add_header("Content-Disposition","attachment", filename=basename(f))
		msg.attach(part)
	
	smtp=smtplib.SMTP(server)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.close()