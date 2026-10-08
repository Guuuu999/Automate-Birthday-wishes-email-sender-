import pandas
import random
from smtplib import *
import datetime as dt
# 1. Update the birthdays.csv
# with open("birthdays.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Erin", "969108723@qq.com", 1990, 4, 15])
now = dt.datetime.now()
month = now.month
today = now.day

data = pandas.read_csv("birthdays.csv")
month_day_list = data[["name", "email", "month", "day"]].to_dict(orient="records")

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letters)

for i in month_day_list:
    if i['month'] == month and i['day'] == today:
        name = i['name']
        with open(random_letter, "r") as file2:
            content = file2.read()

        with open(f"letter_for_{name}", "w") as bw:
            l_content = content.replace("[NAME]", name)

        my_email = "your_email"
        pwd = "your_password"
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=pwd)
            connection.sendmail(from_addr=my_email, to_addrs=i['email'],
                                    msg=f'{l_content}')

# method 2 more simplified
# today = (dt.datetime.now().month, dt.datetime.now().day)
# data = pandas.read_csv("birthdays.csv")
# birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
# if today in birthday_dict:
#     birthday_person = birthday_dict[today]
#     file_path = f"letter_{random.randint(1,3)}.txt"
#     with open(file_path) as file:
#         contents = file.read()
#         contents = contents.replace("[NAME]", birthday_person['name'])


