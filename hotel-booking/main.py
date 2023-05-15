import pandas as pd


df = pd.read_csv('hotels.csv', dtype={"id": str})
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


if __name__ == "__main__":
    hotel_id = input("Enter the id of the hotel:")
    hotel = Hotel(hotel_id)

    if hotel.available():
        hotel.book()
        name = input("Enter your name:")
        reservation = ReservationTicket(customer_name=name, hotel=hotel)
        reservation.generate()
    else:
        print("Hotel is completely sold out!!")

