import pandas as pd
from fpdf import FPDF

class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df['name'].loc[df['id'] == hotel_id].squeeze()

    def list(self):

        pass

    def book(self):
        df['available'].loc[df['id'] == self.hotel_id] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):

        status = df['available'][df['id'] == self.hotel_id].squeeze()

        if status == 'yes':
            return True

        else:
            return False

class Receipt:

    def __init__(self, hotel_name, customer_name):
        self.hotel_name = hotel_name
        self.customer_name = customer_name

    def generate(self):

        pdf = FPDF(orientation='P',unit='mm',format='A4')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()
        pdf.set_font(family='Times',style='B',size=14)
        pdf.cell(w=100, h=8, txt=f"Thank you for your reservation!", align='L', ln=1, border=0)
        pdf.cell(w=100, h=8, txt=f"Your reservation details are as follows:", align='L', ln=1, border=0)
        pdf.cell(w=100, h=8, txt="", align='L', ln=1, border=0)
        pdf.set_font(family='Times',style='',size=12)
        pdf.cell(w=100, h=8, txt=f"Customer Name: {self.customer_name}", align='L', ln=1, border=0)
        pdf.cell(w=100, h=8, txt=f"Hotel: {self.hotel_name}", align='L', ln=1, border=0)
        pdf.set_font(family='Times',style='B',size=11)
        pdf.cell(w=100, h=8, txt=f" ", align='L', ln=1, border=0)
        pdf.cell(w=100, h=8, txt=f"We look forward to your visit!", align='L', ln=1, border=0)
        pdf.output('receipt.pdf')


        
        content = f"""
            Thank you for your reservation!
            Your reservation details are as follows:

            Name: {self.customer_name}
            Hotel: {self.hotel_name}

                """
        
        return content

df = pd.read_csv('hotels.csv', dtype={'id':str})

print(df)

hotel_ID = input("Please Enter Hotel ID: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    customerName = input("Please Enter Your Name and Surname: ")
    customer_receipt = Receipt(hotel_name=hotel.name, customer_name=customerName)
    receipt = customer_receipt.generate()
    print(receipt)

else: 
    print("Hotel is not available")