from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

uri = 'postgresql://{user}:{password}@{host}:{port}/{db}'.\
    format(user="postgres",password="my_password",host="localhost",port="54320",db="postgres")

app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)


class FlaskSQLAlchemyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    dob = db.Column(db.Date)

    def __repr__(self):
        print(self.id+" "+self.username+" "+self.dob)


db.create_all()

admin = FlaskSQLAlchemyTable(username='test1',dob='1971-01-01')
db.session.add(admin)
db.session.commit()
db.session.close()