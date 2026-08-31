import os
import requests
import uuid
import smtplib
import time
from email.message import EmailMessage
from dotenv import load_dotenv 

load_dotenv()

class GmailSender:
    print("------------------------------------------------------------------------------------")
    print(r"""
                ██████╗ ███╗   ███╗ █████╗ ██╗██╗     
                ██╔════╝ ████╗ ████║██╔══██╗██║██║     
                ██║  ███╗██╔████╔██║███████║██║██║     
                ██║   ██║██║╚██╔╝██║██╔══██║██║██║     
                ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗
                ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝

                            GMAIL SENDER by sio87
                """)
    print("------------------------------------------------------------------------------------")
    def __init__(self):
        self.gmail_address = os.getenv("GMAIL_ADDRESS")
        self.gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
    def send_email(self):
         recipient = input("TO: ")
         subject = input("SUBJECT: ")
         message = input("MESSAGE: ")
         times=int(input("HOW MANY TIMES YOU WANT TO SEND IT?: "))


         email = EmailMessage()
         email["From"] = self.gmail_address
         email["To"] = recipient
         email["Subject"] = subject
         email.set_content(message)

         count = 0

         try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
               smtp.login(
                     self.gmail_address,
                     self.gmail_app_password
               )
               while count < times:
                  count += 1 
                  smtp.send_message(email)
                  print(f"[{count}] ✓ EMAIL SENT SUCCESSFULLY to {recipient}!")
                  time.sleep(1)
            
            print("-------------------------------- ALL EMAILS SENT --------------------------------")

         except Exception as error:
               print(f"✗ FAILED TO SEND EMAIL #{count + 1}")
               print("ERROR:", error)
sender = GmailSender()
sender.send_email()