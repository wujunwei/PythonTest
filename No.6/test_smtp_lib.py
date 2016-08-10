import smtplib
from email.mime.text import MIMEText


def sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = "heck@none.com"
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.163.com')
        smtpServer.set_debuglevel(1)
        print("[+] Connecting!")
        smtpServer.ehlo()
        print("[+] start encrypted")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server")
        smtpServer.login(user, pwd)
        print("[+] sending Mail")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
    except Exception as e:
        print(e)

From = "15651757672@163.com"
password = "QWERTYUIOP123"
sendMail(From, password, "15651757672@163.com", 'Re: Important', 'Test Server')

