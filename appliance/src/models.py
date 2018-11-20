"""Models for the firewall appliance database"""

from flask_sqlalchemy import SQLAlchemy
import bcrypt

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
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        return hashed

    @staticmethod
    def verify_hash(password, hash):
        """Verify password and stored password hash match"""
        return hash == bcrypt.hashpw(password.encode('utf8'), hash)


class IPModel(DB.Model):
    __tablename__ = "iptable"

    id = DB.Column(DB.Integer, primary_key=True)
    lt = DB.Column(DB.String(2), unique=False, nullable=False)
    ipv4 = DB.Column(DB.String(120), unique=True, nullable=True)
    ipv6 = DB.Column(DB.String(120), unique=True, nullable=True)
    start_date = DB.Column(DB.String(120), unique=False, nullable=True)
    end_date = DB.Column(DB.String(120), unique=False, nullable=True)
    comments = DB.Column(DB.String(120), unique=False, nullable=True)
    active = DB.Column(DB.Boolean, unique=False, nullable=True)
    remove = DB.Column(DB.Boolean, unique=False, nullable=False)
    geo = DB.Column(DB.Boolean, unique=False, nullable=False)

    def save(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    @classmethod
    def exists(cls, new_ip, ltype):
        if ":" in new_ip:
            return cls.query.filter_by(ipv6=new_ip, lt=ltyp).first()
        return cls.query.filter_by(ipv4=new_ip, lt=ltype).first()

    @classmethod
    def get_all_ip(cls, ltype):
        ips = set()
        all_ip_objects = cls.query.filter_by(lt=ltype, geo=False).order_by(cls.ipv6).all() +\
            cls.query.filter_by(lt=ltype, geo=False).order_by(cls.ipv4).all()
        for cur_ip in all_ip_objects:
            if not cur_ip.ipv4:
                ips.add((str(cur_ip.id), cur_ip.ipv6))
            else:
                ips.add((str(cur_ip.id), cur_ip.ipv4))
        ret = list(ips) if ips else []
        return ret

    @classmethod
    def search(cls, filter_exp, ltype):
        if "." in filter_exp:
            return cls.query.filter_by(ipv4=filter_exp, lt=ltype).first()
        return None

    @classmethod
    def get_entry(cls, id, ltype):
        info = cls.query.filter_by(id=id, lt=ltype).first()
        if info:
            return info
        else:
            return None

    @classmethod
    def update_entry(cls, id, data, ltype):
        entry = cls.query.filter_by(id=id, lt=ltype).first()
        if entry:
            entry.lt=ltype
            entry.ipv4=data['IPv4']
            entry.ipv6=data['IPv6']
            entry.start_date=data['Start_Date']
            entry.end_date=data['End_Date']
            entry.comments=data['Comments']
            active = entry.active
            if data["Active"]:
                if data["Active"].lower() is "false" or data["Active"] is "0":
                    active = False
                elif data["Active"].lower() is "true" or data["Active"] is "1":
                    active = True
            entry.active=active
            DB.session.commit()
            return entry.id
        else:
            return None

    @classmethod
    def delete_entry(cls, id, ltype):
        entry = cls.query.filter_by(id=id, lt=ltype).first()
        if entry:
            entry.remove = True
            DB.session.commit()
            return entry.id
        else:
            return None

    @classmethod
    def get_info(cls, entry):
        if "." in entry:
            return cls.query.filter_by(ipv4=entry).first()
        return None

class GeoModel(DB.Model):
    __tablename__ = "geotable"
    id = DB.Column(DB.Integer, primary_key=True)
    cc = DB.Column(DB.String(2), unique=True, nullable=False)
    lt = DB.Column(DB.String(2), unique=False, nullable=False)
    start_date = DB.Column(DB.String(120), unique=False, nullable=True)
    end_date = DB.Column(DB.String(120), unique=False, nullable=True)
    comments = DB.Column(DB.String(120), unique=False, nullable=True)
    active = DB.Column(DB.Boolean, unique=False, nullable=True)
    remove = DB.Column(DB.Boolean, unique=False, nullable=False)

    @classmethod
    def get_all_geo(cls, ltype):
        geos = set()
        all_geo_objects = cls.query.filter_by(lt=ltype).order_by(cls.cc).all()
        for cur_geo in all_geo_objects:
            geos.add(str(cur_geo.id)+"#"+cur_geo.cc)
        ret = list(geos) if geos else []
        return ret

    @classmethod
    def exists(cls, ccode):
        return cls.query.filter_by(cc=ccode).first()

    @classmethod
    def get_entry(cls, id, ltype):
        info = cls.query.filter_by(id=id, lt=ltype).first()
        if info:
            return info
        else:
            return None

    @classmethod
    def update_entry(cls, id, data, ltype):
        entry = cls.query.filter_by(id=id, lt=ltype).first()
        if entry:
            entry.lt=ltype
            entry.cc = data['CountryCode']
            entry.start_date=data['Start_Date']
            entry.end_date=data['End_Date']
            entry.comments=data['Comments']
            active = entry.active
            if data["Active"]:
                if data["Active"].lower() is "false" or data["Active"] is "0":
                    active = False
                elif data["Active"].lower() is "true" or data["Active"] is "1":
                    active = True
            entry.active=data["Active"]
            DB.session.commit()
            return entry.id
        else:
            return None

    @classmethod
    def delete_entry(cls, id, ltype):
        entry = cls.query.filter_by(id=id, lt=ltype).first()
        if entry:
            entry.remove = True
            entry.id = (entry.id*-1)
            DB.session.commit()
            return entry.id
        else:
            return None

    def save(self):
        DB.session.add(self)
        DB.session.commit()
