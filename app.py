from os import getenv
from twitoff import app, db
from twitoff.models import User
from flask import render_template, request
from twitoff.predict import predict_user
from twitoff.twitter import update_all_users


@app.route("/")
def index():
    return render_template("base.html", title="Home", users=User.query.all())

@app.route("/compare", methods=["POST"])    
def compare(message=""):
    user1 = request.values['user1']
    user2 = request.values['user2']
    tweet_text = request.values['tweet_text']

    if user1 == user2:
        message = "Cannot compare a user to themselves."
    else:
        prediction = predict_user(user1, user2, tweet_text)
        message = f'{tweet_text} is more likely to be said ' \
                  f'by {user1 if prediction else user2} '   \
                  f'than {user2 if prediction else user1}'
        

    return render_template("predict.html", title="Prediction", message=message)


@app.route("/update")
def update():
    update_all_users()
    return render_template("base.html", title="All Tweets Updated", users=User.query.all())


@app.route("/reset")
def reset():
    db.drop_all()
    db.create_all()
    return render_template("base.html", title="Reset Database!", users=User.query.all())


if __name__ == "__main__":
    app.run()
