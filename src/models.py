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


class IPModel(db.Model):
  __tablename__ = "firewall"

  id = db.Column(db.Integer, primary_key = True)
  ipv4 = db.Column(db.String(120), unique = True, nullable = True)
  ipv6 = db.Column(db.String(120), unique = True, nullable = True)
  start_date = db.Column(db.String(120), unique = False, nullable = True)
  end_date = db.Column(db.String(120), unique = False, nullable = True)
  comments = db.Column(db.String(120), unique = False, nullable = True)
  active = db.Column(db.Boolean, unique = False, nullable = True)
  access_list = db.Column(db.String(120), unique = False, nullable = False)
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def exists_in_database(cls, ip):
    if ":" in ip:
      return cls.query.filter_by(ipv6 = ip).first()
    else:
      return cls.query.filter_by(ipv4 = ip).first()
  
  @classmethod
  def get_all_ip(cls):
    ips = set()
    all_ip_objects = cls.query.order_by(cls.ipv6).all() + cls.query.order_by(cls.ipv4).all()
    for ip in all_ip_objects:
      if not ip.ipv4:
        ips.add(ip.ipv6)
      else:
        ips.add(ip.ipv4)
    return list(ips)
      
