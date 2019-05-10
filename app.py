from flask import Flask, render_template, redirect
from datetime import datetime
from flask_pymongo import PyMongo
from scrape_mars import scrape
import os

#initialize Flask
app = Flask(__name__)

#init PyMongo Database
#conn = "mongodb://localhost:27017/mars_app"
#client = pymongo.MongoClient(conn)

#Connect to DB and collection
#db = client.mars_scrape
#collection= db.mars_facts
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


#################INDEX PAGE#############3
@app.route('/')
def home(rerender=False):
    data = mongo.db.mars.find_one()
    #data = collection.find_one()
    print(data)
    return render_template("index.html", data=data, rerender=rerender)

@app.route('/scrape')
def run_scrape():
    results = scrape()
    #remove old record
    #collection.remove({})
    #collection.insert_one(results)
    return redirect('/') 

if __name__ == "__main__":
    app.run(debug=True)