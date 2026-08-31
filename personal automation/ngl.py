import requests
import uuid
import time

class ngl_bomber:
   print("------------------------------------------------------------------------------------")
   print(r"""
                   _   _  ____ _         ____   ___  __  __ ____  _____ ____  
                  | \ | |/ ___| |        | __ ) / _ \|  \/  | __ )| ____|  _ \ 
                  |  \| | |  _| |        |  _ \| | | | |\/| |  _ \|  _| | |_) |
                  | |\  | |_| | |___     | |_) | |_| | |  | | |_) | |___|  _ < 
                  |_| \_|\____|_____|    |____/ \___/|_|  |_|____/|_____|_| \_\  

                              B Y   S I O 87
         """)
   print("------------------------------------------------------------------------------------")
   def ngl():
      USERNAME=input("ENTER THE USERNAME TO BOMB: ")
      MESSAGE=input("ENTER A MESSAGE: ").upper()
      TIMES=int(input("ENTER A NUMBER OF TIMES YOU WANT TO SEND: "))
         
      count=0
      total=0
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
               time.sleep(1)

               if count == TIMES:
                  totals=total+count
                  print("TOTAL MESSAGES SENT:",[totals])
                  print('----------------------------------------------------------------')
                  break

            except requests.RequestException as e:
               print(f"BOMBED FAILED {count + 1}", e)
               print('----------------------------------------------------------------')
ngl_bomber.ngl()