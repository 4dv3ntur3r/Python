import smtplib
import datetime as dt
import random
#
MY_EMAIL = "t3st.drag0n@gmail.com"
PASSWORD = "Killershark@098"
# # for yahoo
# # connection = smtplib.SMTP("smtp.mail.yahoo.com")
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="test.dragon@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# date = now.day
#
# date_of_birth = dt.datetime(year=1994, month=12, day=15)
#
# print(now)

now = dt.datetime.now()
day_of_week = now.weekday()

quotes = []

# One way of doing this
# with open("quotes.txt") as file:
#     for line in file:
#         line = line.split('"')
#         quotes.append(line)
#
# for a in quotes:
#     del a[0]

if day_of_week == 0:
    with open('quotes.txt') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    #random_choice = quotes[random.randrange(len(quotes))]
    # for yahoo
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Morning Quote\n\n{quote}"
        )