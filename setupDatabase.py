import sqlalchemy
import RisingStar.models as models
from RisingStar import create_website

app = create_website()

engine = models.base.db.get_engine()
models.Merchandise.__table__.create(engine)
models.db.session.commit()
print("created merchandise")
if not models.merch_has_values():
    print("adding values to merch")
    models.add_merch()
    models.db.session.commit()
