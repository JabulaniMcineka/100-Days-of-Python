from multiprocessing.dummy import connection
from random import random
import smtplib
import pandas as pd

# my_email = "mjeymcineka@gmail.com"
# password = "mjeymcineka@123"  


# with smtplib.SMTP("smtp.mail.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="recipient@gmail.com",
#         msg="Subject: Happy Birthday!\n\nHappy birthday to you!"
#     )

import datetime as dt
  
  
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_Of_birth = dt.datetime(year=1999, month=6, day=15)

# print(date_Of_birth)



# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# #date_Of_birth = dt.datetime(year=1999, month=6, day=15)

#print(date_Of_birth)

import random

# with open("Day 32/Birthday Wisher (Day 32) start/quotes.txt", "r") as f:
#     random_line = random.choice(f.readlines())
# print(random_line.strip())


df = pd.read_csv("Day 32/Birthday Wisher (Day 32) start/quotes.txt")
selected_quote = random.choice(df['quote'].values)
print(selected_quote)


#Read all lines into a list
with open("file.txt", "r") as file:
    text = file.read()



#Read all lines into a list
with open("file.txt", "r") as file:
    lines = file.readlines()


#Process one line at a time 
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())


#Pick a random line
import random
with open("quotes.txt", "r") as file:
    quote = random.choice(file.readlines()).strip()

print(quote)