#! /usr/bin/python3

import requests
import subprocess
from email.message import EmailMessage
from datetime import datetime
import smtplib
import sys

def main():
    now = datetime.now()
    f = open("text.txt", "a")
    f.write(f"\nNow is {now}")
    f.close()
    try:
        r = requests.get("http://171.235.26.161:8085/health")
        if r.json()['scheduler']['status'] == 'unhealthy':
            # subprocess.run('/home/biserver/airflow-localEX/stack/restart.sh', shell=True, check=True)
            #Email connection
            print("AIRFLOW NOT HEALTHY")
            EMAIL_ADDRESS = 'report@merapgroup.com'
            EMAIL_PASSOWRD = 'Report@111'
            msg = EmailMessage()
            # FROM EMAIL
            msg['From'] = EMAIL_ADDRESS
            # TO EMAIL
            msg['To'] = ['duyvq@merapgroup.com', 'vanquangduy10@gmail.com']
            # BODY
            msg.set_content('AIRFLOW DIED')
            msg['Subject'] = '[ALERT] AIRFLOW DIED'
            with smtplib.SMTP_SSL('mail.merapgroup.com', 465) as smtp:
                conn_smtp = smtp.login(EMAIL_ADDRESS, EMAIL_PASSOWRD)
                print(conn_smtp)
                smtp.send_message(msg)
                print('Message has been sent')
        else: print("Nothing")
    except Exception as err:
        f = open("text.txt", "a")
        f.write(f"\nFAIL is {now}")
        f.close()
        print("NO PORT")
        # subprocess.run('/home/biserver/airflow-localEX/stack/restart.sh', shell=True, check=True)
        #Email connection
        print("AIRFLOW NOT HEALTHY")
        EMAIL_ADDRESS = 'report@merapgroup.com'
        EMAIL_PASSOWRD = 'Report@111'
        msg = EmailMessage()
        # FROM EMAIL
        msg['From'] = EMAIL_ADDRESS
        # TO EMAIL
        msg['To'] = ['duyvq@merapgroup.com', 'vanquangduy10@gmail.com']
        # BODY
        msg.set_content('AIRFLOW DIED')
        msg['Subject'] = '[ALERT] AIRFLOW DIED NO PORT'
        with smtplib.SMTP_SSL('mail.merapgroup.com', 465) as smtp:
            conn_smtp = smtp.login(EMAIL_ADDRESS, EMAIL_PASSOWRD)
            print(conn_smtp)
            smtp.send_message(msg)
            print('Message has been sent')

if __name__ == '__main__':
    main()

