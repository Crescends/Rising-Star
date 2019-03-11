import sqlalchemy
import RisingStar.models as models
from RisingStar import create_website

def setup_database():
    app = create_website()
    engine = models.base.db.get_engine()
    models.db.drop_all()
    models.db.create_all()
    models.add_merch()