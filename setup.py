import sqlalchemy
import RisingStar.models as models
from RisingStar import create_website

def setup_datbase():
    app = create_website()
    engine = models.base.db.get_engine()
    try:
        models.Merchandise.__table__.create(engine)
    except:
        models.Merchandise.__table__.drop(engine)
        models.Merchandise.__table__.create(engine)
        pass
    models.db.session.commit()

    print("created merchandise")
    if not models.merch_has_values():
        print("adding values to merch")
        models.add_merch()
        models.db.session.commit()
    print(models.Merchandise.query.all())
