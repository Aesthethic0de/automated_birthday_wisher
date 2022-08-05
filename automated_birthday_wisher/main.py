
# import smtplib

# import os

# from dotenv import load_dotenv
# load_dotenv()

# my_email = os.environ['my_email']
# password = os.environ['password']

# with smtplib.SMTP("smtp.gmail.com") as cn:
#     cn.starttls()
#     cn.login(user=my_email, password=password)
#     cn.sendmail(from_addr=my_email
#     , to_addrs=my_email,
#      msg="Subject:hello \n\n this is the body of message---> happy birthday",)
#     cn.close()



import random
import datetime as dt
import smtplib
import os

from dotenv import load_dotenv

load_dotenv()

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:

    with open("/home/someetsingh/python_projects/automated_birthday_wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    

    with smtplib.SMTP('smtp.gmail.com') as con:
        con.starttls()
        con.login(user=os.environ['my_email'], password=os.environ['password'])
        con.sendmail(from_addr=os.environ['my_email'], to_addrs=os.environ['to_email'], msg=f"Subject:Friday Motivation\n\n{quote}")
        print("message sent successfully")





