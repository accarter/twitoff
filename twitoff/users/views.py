from flask import Blueprint, render_template, redirect, url_for, request
from twitoff import db
from twitoff.models import User
from twitoff.users.forms import AddForm
from twitoff.twitter import add_user_tweepy

users_blueprint = Blueprint(
    "user", __name__, template_folder="templates/users")

@users_blueprint.route("", methods=["POST"])
@users_blueprint.route("/<name>", methods=["GET"])
def add_or_update_user(name=None, message=""):
    if name is None:
        name = request.values["user_name"]

    try:
        if request.method == "POST":
            add_user_tweepy(name)
            message = "User {} successfully added!".format(name)
        tweets = User.query.filter(User.username == name).one().tweets
    
    except Exception as e:
        print('Error processing {}: {}'.format(name, e))
        tweets = []

    kwargs = dict(title=name, message=message, tweets=tweets)
    return render_template("user.html", **kwargs)


# @users_blueprint.route("/")
# def index():
#     users = User.query.all()
#     return render_template("user.html", users=users)


# @users_blueprint.route("/add", methods=["GET", "POST"])
# def add():
#     form = AddForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None:
#             db.session.add(User(username=form.username.data,
#                             followers=form.followers.data))
#             db.session.commit()

#             return redirect(url_for("users.index"))

#     return render_template("add_user.html", form=form)
