import psycopg2
import requests
import smtplib
import time

api_key = 'asdfadsf adsf af'

email = input("Enter email ID:")
password = input("Enter Password:")
n = input("Enter the BTC stock amount: ")



def send_mail(password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    subject = 'BTC Stock Alert!'
    body = 'Price has reached the amount!'

    msg = f'subject: {subject} {body}'

    server.sendmail(
        email,
        email,
        msg
    )
    print('Email is sent to user!')
    server.quit()


def price_tracker(api_key, password):
    prices = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    stockPrice = prices[0]['current_price']
    print(stockPrice)
    if stockPrice < int(n) :
        send_mail(password)


# run evrey 10 minutes
while (True):
    price_tracker(api_key, password)
    time.sleep(600)

conn = psycopg2.connect(
     database="StockData", user='postgres', password='9091', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()
cursor.execute('''INSERT INTO 'Stock'(Email,Password,Amount) VALUES ('email', 'password', 'n')''')

conn.commit()
print("Records inserted!")

# Closing the connection
conn.close()