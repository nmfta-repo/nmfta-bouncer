"""Models for the firewall app database"""

from passlib.hash import sha256_crypt as sha256
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class UserModel(DB.Model):
    """User model for app database"""
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(120), unique=True, nullable=False)
    password = DB.Column(DB.String(120), nullable=False)

    def save(self):
        """Save the current user profile to the database"""
        DB.session.add(self)
        DB.session.commit()

    @classmethod
    def lookup_user(cls, username):
        """Find a user based on username"""
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def gen_hash(password):
        """Securly hash the password to check"""
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """Verify password and stored password hash match"""
        return sha256.verify(password, hash)


class IPModel(DB.Model):
    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    ipv4 = DB.Column(DB.String(120), unique=True, nullable=True)
    ipv6 = DB.Column(DB.String(120), unique=True, nullable=True)
    start_date = DB.Column(DB.String(120), unique=False, nullable=True)
    end_date = DB.Column(DB.String(120), unique=False, nullable=True)
    comments = DB.Column(DB.String(120), unique=False, nullable=True)
    active = DB.Column(DB.Boolean, unique=False, nullable=True)

    def save(self):
        DB.session.add(self)
        DB.session.commit()

    @classmethod
    def exists(cls, new_ip):
        if ":" in new_ip:
            return cls.query.filter_by(ipv6=new_ip).first()
        return cls.query.filter_by(ipv4=new_ip).first()

    @classmethod
    def get_all_ip(cls):
        ips = set()
        all_ip_objects = cls.query.order_by(cls.ipv6).all() + cls.query.order_by(cls.ipv4).all()
        for cur_ip in all_ip_objects:
            if not cur_ip.ipv4:
                ips.add(cur_ip.ipv6)
            else:
                ips.add(cur_ip.ipv4)
        ret = list(ips) if ips else []
        return ret

    @classmethod
    def search(cls, filter_exp):
        if "." in filter_exp:
            return cls.query.filter_by(ipv4=filter_exp).first()
        return None


    @classmethod
    def get_info(cls, entry):
        if "." in entry:
            return cls.query.filter_by(ipv4=entry).first()
        return None


class WLModel(IPModel):
    __tablename__ = "whitelist"

class BLModel(IPModel):
    __tablename__ = "blacklist"
