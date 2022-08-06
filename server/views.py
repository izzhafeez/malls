from flask import jsonify
import pandas as pd

from server import app, db
from server.models import Mall

@app.route("/")
def index():
  return "Hello"

@app.route("/malls/populate")
def populate_all():
  db.drop_all()
  db.create_all()
  malls_records = pd.read_csv("server/data/malls.csv").to_dict("records")
  for record in malls_records:
    mall = Mall(
      name=record["name"],
      lat=record["lat"],
      lon=record["lon"],
      station=record["station"],
      colors=record["colors"],
      services=record["services"],
      halals=record["halals"],
      stores=record["stores"],
      floors=record["floors"],
      retail_area=record["retail_area"],
      opening_year=record["opening_year"]
    )
    db.session.add(mall)
  db.session.commit()
  return {"malls": malls_records}

@app.route("/malls/<name>")
def get_mall(name):
  mall_dict = Mall.query.filter_by(name=name.replace("%20", " ")).first().as_dict()
  mall_dict["colors"] = mall_dict["colors"].split(",")
  return mall_dict
  
    