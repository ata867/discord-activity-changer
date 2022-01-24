import requests
import time
from secret import header # Create a secret.py file with header containing your discord authorization token

payload = {"custom_status":{
    "emoji_name": "", # Status emoji
    "text": ""
}}

endpoint = "https://discord.com/api/v9/users/@me/settings"

def main():
    i = 0
    while True:
        with open("./activity.txt", "r") as r:
            for line in r:
                line = line.rstrip() # Remove blank spaces
                if line == "" : continue # Continue if blank line
                payload["custom_status"]["text"] = line
                r = requests.patch(endpoint, json=payload, headers=header)
                if r.status_code != 200 : break
                time.sleep(0.5) # Interval

def reset(): # Reset status
    payload["custom_status"]["text"], payload["custom_status"]["emoji_name"] = "", ""
    r = requests.patch(endpoint, json=payload, headers=header)

if __name__ == "__main__":
    main()