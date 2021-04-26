from flask import Flask, render_template, jsonify, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://zrdhklredtuzxs' \
                                 ':f9566c90e9c40501d67cfa78f2c88630f073e0fe82412ca3bd54e93201de7e2d@ec2-52-87-107-83' \
                                 '.compute-1.amazonaws.com:5432/dbjfa8nmv46bji '

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return redirect(url_for('index'))


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email = data["email"]

        new_data = User(name, email)
        db.session.add(new_data)
        db.session.commit()

        user_data = User.query.all()

        return render_template("index.html", user_data=user_data)

    return render_template("index.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
