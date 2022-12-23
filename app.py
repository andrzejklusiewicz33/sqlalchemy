from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://asseco_dev:oracle@localhost/asseco"
db=SQLAlchemy(app)

class ChristmasDish(db.Model):
    __tablename__="christmas_dishes"
    cd_id=db.Column(db.Integer, name="cd_id", primary_key=True, autoincrement=True)
    name=db.Column(db.String,name="name")
    description=db.Column(db.String, name="description", nullable=True)
    weight=db.Column(db.Integer,name="weight", nullable=True, index=True)

@app.route('/create_db')
def create_db():
    db.create_all()
    return "ok"

@app.route('/')
def hello_world():  # put application's code here
    #print(app.config)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,port=80)

#76. Stwórz nowy projekt we Flask. Dodaj do niego obsługiwaną przez SQLAlchemy klasę encyjną
#Product posiadająca id,nazwę,cenę i opis. Dodaj ekran którego wywołanie spowoduje stworzenie
#tabelki w bazie danych. Wejdz na ten ekran i upewnij się że tabelka powstała.