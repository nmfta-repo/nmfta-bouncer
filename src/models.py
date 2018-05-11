from database import db
from passlib.hash import sha256_crypt as sha256

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def lookup_user(cls, username):
        return cls.query.filter_by(username = username).first()

    @staticmethod
    def gen_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class IPModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    ipv4 = db.Column(db.String(120), unique = True, nullable = True)
    ipv6 = db.Column(db.String(120), unique = True, nullable = True)
    start_date = db.Column(db.String(120), unique = False, nullable = True)
    end_date = db.Column(db.String(120), unique = False, nullable = True)
    comments = db.Column(db.String(120), unique = False, nullable = True)
    active = db.Column(db.Boolean, unique = False, nullable = True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def exists(cls, ip):
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
        ret = list(ips) if len(ips) > 0 else []
        return ret

    @classmethod
    def search(cls, filter):
        if "." in filter:
            return cls.query.filter_by(ipv4=filter).first()


    @classmethod
    def get_info(cls, entry):
        if "." in filter:
            return cls.query.filter_by(ipv4=filter).first()


class WLModel(IPModel):
    __tablename__ = "whitelist"

class BLModel(IPModel):
    __tablename__ = "blacklist"
