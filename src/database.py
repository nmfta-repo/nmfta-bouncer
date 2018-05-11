from flask_sqlalchemy import SQLAlchemy

db = None

def init_db(app):
	#Database setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'some-secret-string'	#should also probably change this
    global db
    db = SQLAlchemy(app)

    from models import UserModel
    from models import WLModel
    from models import BLModel
    db.create_all()


def clear_data():
    global db
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print 'Clear table %s' % table
        db.session.execute(table.delete())
    db.session.commit()
