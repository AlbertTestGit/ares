import datetime
import random
import csv


def random_name():
    names = []

    with open('data/name.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            _t = ', '.join(row)
            names.append(_t.replace('"', ''))

    return names[random.randint(0, len(names) - 1)]


def random_surname():
    surnames = []

    with open('data/surname.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            _t = ', '.join(row)
            surnames.append(_t.replace('"', ''))

    return surnames[random.randint(0, len(surnames) - 1)]


def random_card_number():
    num = '4410'
    rnd = random.randint(1000_0000_0000, 9999_9999_9999)
    return f'{num}{rnd}'


def random_expire_date():
    current_year = datetime.date.today().year - 2000
    current_month = datetime.date.today().month

    mm = current_month + random.randint(1, 12 - current_month)
    yy = current_year + random.randint(0, 4)

    return f'{mm:02}/{yy}'


def random_cvv():
    return f"{random.randint(0,999):03}"


def random_amount():
    return random.randint(1, 50) * 500


def random_email():
    emails = []

    with open('data/email.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            _t = ', '.join(row)
            emails.append(_t.replace('"', ''))

    return emails[random.randint(0, len(emails) - 1)]
