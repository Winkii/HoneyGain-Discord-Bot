from datetime import datetime, timedelta, timezone

def convert_cents_to_dollars(raw_price):
  price = int(raw_price)/100
  return price

def convert_credits_to_money(credit):
  money=credit/1000
  #Format to 2 decimal places
  return "{0:.2f}".format(money)



