from flask_sqlalchemy import SQLAlchemy

db = None

def init_db(app):
  #Database setup
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firewall.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = 'some-secret-string'                   #MODIFY
  global db  
  db = SQLAlchemy(app)
  
  from models import UserModel
  db.create_all()


def clear_data():
  global db
  meta = db.metadata
  for table in reversed(meta.sorted_tables):
    print 'Clear table %s' % table
    db.session.execute(table.delete())
  db.session.commit()
