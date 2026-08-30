import requests
import uuid


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
         MESSAGE=input("ENTER A MESSAGE: ")
         TIMES=int(input("ENTER A NUMBER OF TIMES YOU WANT TO SEND: "))
         count=0

         while count < TIMES:
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

                  print("Status:", response.status_code)
                  print("Response:", response.text)
                  print("------------------------------------------------------------------------------------")
               except requests.RequestException as e:
                  print("Request failed:", e)

               if count == TIMES:
                   print("BOMBED SUCCESSFULLY")
                   print('--------------------------------BOMBED SUCCESSFULLY--------------------------------')
ngl_bomber.ngl()
   