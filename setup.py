from RisingStar import create_website
from RisingStar.models import db, Product, Post, User
from csv import DictReader
import locale

locale.setlocale(locale.LC_ALL, '')

def setup_database():
    create_website()
    db.drop_all()
    db.create_all()
    add_products()
    add_dummy_posts()

def add_dummy_posts():
    user = User.query.first()
    print(user)
    a = Post(author=user, title="He is So Hot", content="I just cant stand it anymore last time I saw him I almost creamed my pants")
    db.session.add(a)
    for i in range(10):
        p = Post(author=user, title="Wow Dude U Crazy",content="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi quidem nobis, quis doloremque quam magni nostrum, tempore corporis, non amet sit eius nemo totam voluptas minus laborum reiciendis molestias ducimus.")
        db.session.add(p)
    db.session.commit()

def add_products():
    with open("ProductNames.csv") as f:
        reader = DictReader(f)
        for row in reader:
            name = row["NAME"]
            category = row["CATEGORY"]
            price = float(row["PRICE"])
            ablum_type = name.split(" ")[0]
            display_name = f"{ablum_type} {category}"
            product = Product(album=ablum_type, type=category, cost=locale.currency(price), name=display_name, image_name=name+'.png')
            print(product)
            db.session.add(product)
    db.session.commit()

create_website()
add_dummy_posts()