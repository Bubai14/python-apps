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
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt";
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True, port=8008)
