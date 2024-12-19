import pandas as pd

class Hotel:

    def __init__(self, id):
        pass

    def list(self):
        pass

    def book(self):
        pass

    def available(self):
        pass

class Receipt:

    def __init__(self, hotel_name, customer_name):
        pass

    def generate(self):
        pass

df = pd.read_csv('hotels.csv')

print(df)

hotel_id = input("Please Enter Hotel ID: ")
hotel = Hotel(hotel_id)

if hotel.available() == 'yes':
    hotel.book()
    customer_name = input("Please Enter Your Name and Surname: ")
    customer_receipt = Receipt(hotel, customer_name)
    print(customer_receipt)

else: 
    print("Hotel is not available")