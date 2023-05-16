import pandas as pd


df = pd.read_csv('hotels.csv', dtype={"id": str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv('card_security.csv', dtype=str)
print(df)


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"]

    def book(self):
        df.loc[df['id'] == self.hotel_id, "available"] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        print(content)


class CreditCard:

    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card in df_cards:
            return True
        else:
            return False


class SecuredCreditCard(CreditCard):

    def authenticate(self, password):
        passw = df_card_security.loc[df_card_security['number'] == self.number, "password"].squeeze()
        if passw == password:
            return True
        else:
            return False


if __name__ == "__main__":
    hotel_id = input("Enter the id of the hotel:")
    hotel = Hotel(hotel_id)

    if hotel.available():
        credit_card = SecuredCreditCard("1234")
        if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
            if credit_card.authenticate(password="mypass"):
                hotel.book()
                name = input("Enter your name:")
                reservation = ReservationTicket(customer_name=name, hotel=hotel)
                reservation.generate()
            else:
                print("Credit card authentication failed!!")
        else:
            print("There is a problem with your payment")
    else:
        print("Hotel is completely sold out!!")

