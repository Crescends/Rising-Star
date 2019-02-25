import sqlalchemy
import RisingStar.models as models
from RisingStar import create_website()

app = create_website()

models.base.db.create_all()
if not models.merch_has_values():
    models.add_merch()