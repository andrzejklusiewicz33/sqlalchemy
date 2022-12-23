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
    def __str__(self):
        return str(self.__dict__)


def save_christmas_dish(cd):
    db.session.add(cd)
    db.session.commit()

def get_all_christmas_dishes():
    return ChristmasDish.query.all()

def get_filtered_christmas_dishes():
    #return ChristmasDish.query.filter(ChristmasDish.weight>100).order_by(ChristmasDish.weight.desc()).all()
    return ChristmasDish.query.filter(ChristmasDish.weight > 100).order_by(ChristmasDish.weight).all()
class Product(db.Model):
    __tablename__="products_sqlalchemy"
    product_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String)
    price=db.Column(db.Float)
    description=db.Column(db.String,nullable=True)
    def __str__(self):
        return str(self.__dict__)

def get_products():
    return Product.query.order_by(Product.price.desc()).all()

@app.route('/print_products')
def print_products():
    for p in get_products():
        print(p)
    return "ok"

@app.route('/print_dishes')
def print_dishes():
    for cd in get_filtered_christmas_dishes():
    #for cd in get_all_christmas_dishes():
        print(cd)
    return "ok"


@app.route('/save_dish')
def save_dish():
    cd=ChristmasDish()
    cd.name="pierogi"
    cd.weight=2000
    cd.description="Każdy wie o co kaman z pierogami"
    save_christmas_dish(cd)
    return "ok"

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

#77.Dodaj sobie produkty do bazy. Dodaj ekran - jak na niego wejdziesz to na konsoli
#chcemy zobaczyć wydrukowane linia po linii wszystkie produkty ale posortowane
#malejąco wg. ceny

#reportlab

#78. Dodaj ekran po którego wywołaniu do bazy zostanie dodany nowy produkt