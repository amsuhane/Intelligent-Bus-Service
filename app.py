#!/usr/bin/env python3
from flask import Flask, render_template,url_for,redirect
import os
import json
# from backend import det
import gps

app = Flask(__name__)

people = 0

@app.route('/')
def home():
    json_file = open("./static/data.json")
    json_str = json_file.read()
    data = json.loads(json_str)
    return render_template("index.html", data = data)

@app.route('/index.html')
def index():
    json_file = open("./static/data.json")
    json_str = json_file.read()
    data = json.loads(json_str)
    return render_template("index.html", data = data)

@app.route('/bus/<bus_no>')
def get_bus_info(bus_no):
    json_file = open("./static/data.json")
    json_str = json_file.read()
    data = json.loads(json_str)
    
    no = data["bus" + str(bus_no)]
    return render_template("bus_info.html", no = no, bus_no = bus_no)
    
@app.route('/location.html')
def location():
    global people
    location_stats="Vikramshila"
    loc_img = os.path.join("static", "loc.png")
    if people == 0:
        p = "No processing initiated..."
        loc_img = None
    else:
        p = people

    return render_template("location.html", location_stats=location_stats, number=p, loc_img=loc_img)

if __name__ == "__main__":
    app.run(debug=True)