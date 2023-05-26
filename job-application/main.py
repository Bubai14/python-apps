from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy is a high level database package
import datetime

app = Flask(__name__)
# Create the database on start of the application
app.config["SECRET_KEY"] = "jobapp"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


# Create the table and columns inside the database
class Applicant(db.Model):
    id = db.Column(db.Integer, primaryKey=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        start_date = request.form["start_date"]
        db_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        applicant = Applicant(first_name=first_name, last_name=last_name,
                              email=email, start_date=db_start_date, occupation=occupation)
        db.session.add(applicant)
        db.session.commit()
        flash(f"{first_name}, your application was submitted successfully", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
