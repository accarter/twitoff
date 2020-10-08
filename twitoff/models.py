from twitoff import db


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    followers = db.Column(db.String(120), unique=False, nullable=False)
    tweets = db.relationship('Tweet', backref=db.backref('user'), lazy=True)
    newest_tweet_id = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return '<{__class__.__name__}; username={username}>'\
            .format(__class__=self.__class__, **self.__dict__)


class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(280), unique=False, nullable=False)
    embedding = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return '<{__class__.__name__}; text={text}>'\
            .format(__class__=self.__class__, **self.__dict__)
