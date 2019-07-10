import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

def send_mail(send_from, send_to, subject, text="", html="", files=None, server="127.0.0.1"):
	assert isinstance(send_to, list)
	msg = EmailMessage()
	msg['From'] = send_from
	msg['To'] =', '.join(send_to) 
	msg['Date'] = formatdate(localtime=True) 
	msg['Subject'] = subject
	msg.set_content(text)
		
	msg.attach(MIMEText(text, 'plain'))
	if not html=="":
		msg.add_alternative(html, subtype='html')

	for f in files or []:
		with open(f, 'rb') as fp:
			attachment = fp.read()
			msg.add_attachment(attachment, maintype='text', subtype='txt', filename=f)
	
	smtp=smtplib.SMTP(server)
	smtp.send_message(msg)
	smtp.close()