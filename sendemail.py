import urllib.request as urllib2
from datetime import datetime
from redmail import outlook
import random
def is_connected():
    try:
        urllib2.urlopen('http://142.250.191.100')
        return True
    except urllib2.URLError as err:
        return False
def OTP():
    OTPCODE =''
    for i in range(6):
        OTPCODE = OTPCODE + str(random.randint(0, 9))
    return OTPCODE
def send(emailadd,OTP):


    outlook.user_name = "API_VERIFY@outlook.com"
    outlook.password = "AQ8@hRCS"

    outlook.send(
        receivers=[emailadd],
        subject="Your OTP is ",
        text=OTP)
    print("Email Sent")

def main():
    if is_connected() :
        print("Connected to Internet")
        print(datetime.now())


    else:
         print("Unable to connect to internet ...")

if __name__ == "__main__":
    OTP()