from logging import exception
from multiprocessing import connection
import pandas as pd
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("/home/someetsingh/python_projects/automated_birthday_wisher/birthdays.csv")


birthday_dict = {(data_rows['month'], data_rows['day']): data_rows for (index,data_rows) in data.iterrows()}
try:
    if today_tuple in birthday_dict:
        birthday_person = birthday_dict[today_tuple]
        print(birthday_person)
        file_path = f"/home/someetsingh/python_projects/automated_birthday_wisher/letter_templates/letter_" + str(random.randint(1,3)) + ".txt"
        with open("/home/someetsingh/python_projects/automated_birthday_wisher/quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
        with open(file_path) as file:
            content = file.read()
            content = content.replace("[NAME]", birthday_person['name']) 
            content = content.replace("Angela", "Sunny") + "\n\n" + quote
            print(content)
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=os.environ['my_email'], password=os.environ['password'])
            conn.sendmail(from_addr=os.environ['my_email'], to_addrs=os.environ['my_email'], msg=f"Subject:happy birthday\n\n{content}")
            print(f"message successdully sent to {birthday_person['name']}")

        
except Exception as e:
    print(f"the problem is with {Exception}")


        



