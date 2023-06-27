from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os
import requests
import json
import sqlite3
import cs50
from sqlite3 import Error
load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
db = cs50.SQL("sqlite:////Users/jackdrisdelle/desktop/code/Apex_App/player.db")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # conn = get_db_connection()
        
        # username = request.form.get("player_id")
        # platform = request.form.get("platform")
        username = "PikaPlayzMC3083"
        platform = "X1"

        if not username:
            print("Sorry, need username or username not found")

        if not platform:
            print("Sorry, need platform or platform not found")
            print("use PSN, XBL, Steam, Origin")

        data = lookup(username, platform)
        # print(data)

        # lookup(username, platform)
        print(type(data))
        data_str = json.dumps(data)
        print(type(data_str))
        data_json = json.loads(data_str)
        db.execute("insert into players (name, rank, level, platform, uid, legend, frame, pose, badge1, badge2, badge3) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                   data_json['global']['name'],
                   data_json['global']['rank']['rankName'],
                   data_json['global']['level'],
                   data_json['global']['platform'],
                   data_json['global']['uid'],
                   data_json['legends']['selected']['LegendName'],
                   data_json['legends']['selected']['gameInfo']['frame'], 
                   data_json['legends']['selected']['gameInfo']['pose'],
                   data_json['legends']['selected']['gameInfo']['badges'][0]['name'],
                   data_json['legends']['selected']['gameInfo']['badges'][1]['name'],
                   data_json['legends']['selected']['gameInfo']['badges'][2]['name'])
        
        return render_template("playerFound.html", player_data=data_json)

def lookup(player_id, platform_id):
    url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player_id}&platform={platform_id}"
    print(url)
    response = requests.get(url)
    data = response.json()
    return data

