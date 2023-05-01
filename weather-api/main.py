from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("weather-api.html")


@app.route("/home")
def home():
    return render_template("tutorial.html")


@app.route("/about/")
def about():
    return render_template("about.html")


# REST APIs
@app.route("/api/v1/<station>/<date>")
def restapi(station, date):
    temperature = 23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True, port=8008)
