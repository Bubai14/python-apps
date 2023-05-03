import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"


def get_data(place, forecasted_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid=141710af2113bab9f55ef73e1bcd33d5"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # There are 40 records in the response which 5 days of data with 3 hours interval
    # This implies each day = 24/3 = 8, 8 * 5 = 40
    # Now to get the data for the selected days, its 8 * forecasted_days
    filtered_data = filtered_data[:8*forecasted_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Kolkata", forecasted_days=2))
