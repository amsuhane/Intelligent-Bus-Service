#!/usr/bin/env python3
from flask import Flask, render_template,url_for,redirect
import os
from backend import det

app = Flask(__name__)

people = 0

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/bus')
def background_process_test():
    global people
    location_stats = "ABC"
    loc_img = os.path.join("static", "loc.png")
    people = det.get_people()
    # redirect(url_for('/location.html'))
    return render_template("location.html", location_stats=location_stats, number=people, loc_img=loc_img)
    
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