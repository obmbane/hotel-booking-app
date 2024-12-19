import pandas as pd

class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def list(self):

        pass

    def book(self):
        df['available'].loc[df['id'] == self.hotel_id] = 'no'
        df.to_csv('hotels.csv')

    def available(self):

        status = df['available'][df['id'] == self.hotel_id].squeeze()
        print(status)

        if status == 'yes':
            test = 13 + car 
            print(test)
            return True

        else:
            return False

class Receipt:

    def __init__(self, hotel_name, customer_name):
        pass

    def generate(self):
        pass

df = pd.read_csv('hotels.csv', dtype={'id':str})

print(df)

hotel_ID = input("Please Enter Hotel ID: ")
hotel = Hotel(hotel_ID)
car = 31

if hotel.available():
    hotel.book()
    customer_name = input("Please Enter Your Name and Surname: ")
    customer_receipt = Receipt(hotel, customer_name)
    print(customer_receipt)

else: 
    print("Hotel is not available")