from RisingStar import create_website
from RisingStar.models import db, Product
from csv import DictReader
import locale

locale.setlocale(locale.LC_ALL, '')

def setup_database():
    create_website()
    db.drop_all()
    db.create_all()
    add_products()


def add_products():
    with open("ProductNames.csv") as f:
        reader = DictReader(f)
        for row in reader:
            name = row["NAME"]
            category = row["CATEGORY"]
            price = float(row["PRICE"])
            ablum_type = name.split(" ")[0]
            display_name = f"{ablum_type} {category}"
            product = Product(type=category, cost=locale.currency(price), name=display_name, image_name=name+'.png')
            print(product)
            db.session.add(product)
    db.session.commit()
