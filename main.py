import os
import requests
import uuid
import smtplib
import time
from email.message import EmailMessage
from dotenv import load_dotenv 

load_dotenv()

class GmailSender:
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

class ngl_bomber:
   def ngl():
      USERNAME=input("ENTER THE USERNAME TO BOMB: ")
      MESSAGE=input("ENTER A MESSAGE: ").upper()
      TIMES=int(input("ENTER A NUMBER OF TIMES YOU WANT TO SEND: "))
         
      count=0

      while True:
            count < TIMES
            count += 1
            url = "https://ngl.link/api/submit"
            headers = {
                  "Content-Type": "application/x-www-form-urlencoded",
                  "X-Requested-With": "XMLHttpRequest",
                  "User-Agent": "Mozilla/5.0",
                  "Referer": f"https://ngl.link/{USERNAME}",
               }

            data = {
                  "username": USERNAME,
                  "question": MESSAGE,
                  "deviceId": str(uuid.uuid4()),
                  "gameSlug": "",
                  "referrer": "",
               }

            try:
               response = requests.post(
                  url,
                  headers=headers,
                  data=data,
                  timeout=15
               )

               print("MESSAGE SENT TO:",USERNAME)
               print(count,"Status:", response.status_code)
               print(count,"Response:", response.text)
               time.sleep(2)

               if count == TIMES:
                  total=0
                  total.append(count)
                  print("TOTAL MESSAGES SENT:",total)
                  print('----------------------------------------------------------------')

            except requests.RequestException as e:
               print(f"BOMBED FAILED {count + 1}", e)
               print('----------------------------------------------------------------')
 
def choice():
   choice =int(input('CHOOSE A TOOL NUMBER: '))

   if choice == 1:
      print("------------------------------------------------------------------------------------")
      print(r"""
                     _   _  ____ _         ____   ___  __  __ ____  _____ ____  
                     | \ | |/ ___| |        | __ ) / _ \|  \/  | __ )| ____|  _ \ 
                     |  \| | |  _| |        |  _ \| | | | |\/| |  _ \|  _| | |_) |
                     | |\  | |_| | |___     | |_) | |_| | |  | | |_) | |___|  _ < 
                     |_| \_|\____|_____|    |____/ \___/|_|  |_|____/|_____|_| \_\  
            """)
      print("------------------------------------------------------------------------------------")
      ngl_bomber.ngl()
   elif choice == 2:
      sender = GmailSender()
      sender.send_email()
   elif choice == 3:
       print()







print(r"""
         ╔════════════════════════════════════════════════════════════════════════════════════════════════════╗
         ║                                                                                                    ║
         ║   ████████╗ ██████╗  ██████╗ ██╗         ███╗   ███╗███████╗███╗   ██╗██╗   ██╗                    ║
         ║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║         ████╗ ████║██╔════╝████╗  ██║██║   ██║                    ║
         ║      ██║   ██║   ██║██║   ██║██║         ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║                    ║
         ║      ██║   ██║   ██║██║   ██║██║         ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║                    ║
         ║      ██║   ╚██████╔╝╚██████╔╝███████╗    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝                    ║
         ║      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                     ║
         ║                                                                                                    ║
         ║                                      B Y   S I O 8 7                                               ║
         ║                                                                                                    ║
         ╠════════════════════════════════════════════════════════════════════════════════════════════════════╣
         ║   [1] NGL BOMBER                                                                                   ║
         ║   [2] GMAIL SENDER                                                                                 ║
         ║   [3] Project Name                                                                                 ║
         ║   [4] Project Name                                                                                 ║
         ║   [5] Project Name                                                                                 ║
         ║   [6] Project Name                                                                                 ║
         ║   [7] Project Name                                                                                 ║
         ║   [8] Project Name                                                                                 ║
         ║   [9] Project Name                                                                                 ║
         ║   [10] Project Name                                                                                ║
         ╚════════════════════════════════════════════════════════════════════════════════════════════════════╝
      """)
choice()