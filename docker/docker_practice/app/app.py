from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from config import Config
from populate_data import get_users, get_goods, get_stores
from models import User, Good, Store

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print("Database does not exists", {db.engine.url})
        create_database(db.engine.url)  # create db
        print('DB created')

with app.app_context():
    users = get_users()
    for user in users:
        # print(user)
        db.session.add(User(**user))
    db.session.commit()
    print("Data 'users' has already written in database")

with app.app_context():
    goods = get_goods()
    for good in goods:
        # print(good)
        db.session.add(Good(**good))
    db.session.commit()
    print('Data "goods" has already written in database')

with app.app_context():
    stores = get_stores()
    for store in stores:
        #print(store)
        db.session.add(Store(**store))
    db.session.commit()
    print('Data "stores" has already written in database')


