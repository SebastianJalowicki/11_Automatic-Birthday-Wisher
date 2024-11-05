import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = 'xxx@gmail.com'
MY_PASSWORD = 'abc'


def send_email():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg=f'Subject:Happy Birthday!\n\n{contents}'
        )


now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pd.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
    send_email()
