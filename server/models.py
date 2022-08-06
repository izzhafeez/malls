from server import db

class Mall(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  lat = db.Column(db.Float(), nullable=False)
  lon = db.Column(db.Float(), nullable=False)
  station = db.Column(db.String(5), nullable=False)
  colors = db.Column(db.String(100), nullable=False)
  services = db.Column(db.Integer(), nullable=False)
  halals = db.Column(db.Integer(), nullable=False)
  stores = db.Column(db.Integer(), nullable=False)
  floors = db.Column(db.Integer(), nullable=False)
  retail_area = db.Column(db.Integer(), nullable=False)
  opening_year = db.Column(db.Integer(), nullable=False)
  
  def as_dict(self):
    return {
      c.name: getattr(self, c.name) for c in self.__table__.columns
    }  
