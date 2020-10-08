from flask import Blueprint, render_template, redirect, url_for, request
from twitoff import db
from twitoff.models import User, Tweet
from twitoff.tweets.forms import AddForm


tweets_blueprint = Blueprint(
    'tweets', __name__, template_folder='templates/tweets')


@tweets_blueprint.route("/<user_id>")
def index(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template("tweet.html", user=user)


@tweets_blueprint.route("/add/<user_id>", methods=["GET", "POST"])
def add(user_id):
    form = AddForm()

    if form.validate_on_submit():
        db.session.add(Tweet(user_id=user_id,
                             text=form.text.data))
        db.session.commit()

        return redirect(url_for("tweets.index", user_id=user_id))

    return render_template("add_tweet.html", form=form)
