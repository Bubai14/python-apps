from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
stations = pd.read_csv("data_small/stations.txt", skiprows=17)


@app.route("/")
def base():
    return render_template("weather-api.html", station_list=stations.to_html())


@app.route("/home")
def home():
    return render_template("tutorial.html")


@app.route("/about/")
def about():
    return render_template("about.html")


# REST APIs
@app.route("/api/v1/<station>/<date>")
def restapi(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


# Returns all the data of a station
@app.route("/api/v1/<station>")
def all_station_data(station):
    filename = get_station_file(station)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


# Returns data of a station by year
@app.route("/api/v1/year/<station>/<year>")
def yearly_station_data(station, year):
    filename = get_station_file(station)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


def get_station_file(station):
    return "data_small/TG_STAID" + str(station).zfill(6) + ".txt"


if __name__ == "__main__":
    app.run(debug=True, port=8008)
