import pandas as pd
import smtplib
import random
import datetime as dt

MY_EMAIL = "t3st.drag0n@gmail.com"
PASSWORD = "Killershark@098"

df = pd.read_csv('birthdays.csv')

now_month = dt.datetime.now().month
now_date = dt.datetime.now().day

for a in range(len(df)):
    if now_month == df.month[a] and now_date == df.day[a]:
        name = df.name[a]
        email = df.email[a]

        num = random.randint(1,3)
        with open(f'letter_templates/letter_{num}.txt') as letter:
            message = letter.read()
            message = message.replace('[NAME]', name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!!\n\n{message}")





