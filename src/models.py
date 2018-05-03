from database import db
from passlib.hash import sha256_crypt as sha256

class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(120), unique = True, nullable = False)
  password = db.Column(db.String(120), nullable = False)
    
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username = username).first()

  @staticmethod
  def gen_hash(password):
    return sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    return sha256.verify(password, hash)


class WhitelistModel(db.Model):
  __tablename__ = "whitelist"

  id = db.Column(db.Integer, primary_key = True)
  ip = db.Column(db.String(120), unique = True, nullable = False)
