from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os
import requests
import json
import sqlite3
import cs50

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
db = cs50.SQL("sqlite:///player.db")



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        
        username = request.form.get("player_id")
        platform = request.form.get("platform")
        # username = "PikaPlayzMC3083"
        # platform = "X1"

        if not username:
            print("Sorry, need username or username not found")
            return render_template("index.html") + "Sorry, there was an issue with the user."

        if not platform:
            print("Sorry, need platform or platform not found")
            print("use PSN, XBL, Steam, Origin")
            return render_template("index.html") + "Sorry, there was an issue with the platform selection."

        data = lookup(username, platform)
        # print(data)

        # lookup(username, platform)
        print(type(data))
        data_str = json.dumps(data)
        print(type(data_str))
        data_json = json.loads(data_str)
        
        tracker_1_name = None
        tracker_1_value = None
        tracker_2_name = None
        tracker_2_value = None
        tracker_3_name = None
        tracker_3_value = None
        
        


        if len(data_json['legends']['selected']['data'][0]) != None:
            tracker_1_name = data_json['legends']['selected']['data'][0]['name']
            tracker_1_value = data_json['legends']['selected']['data'][0]['value']
        if len(data_json['legends']['selected']['data'][1]) != None:
            tracker_2_name = data_json['legends']['selected']['data'][1]['name']
            tracker_2_value = data_json['legends']['selected']['data'][1]['value']
        if len(data_json['legends']['selected']['data'][2]) != None:
            tracker_3_name = data_json['legends']['selected']['data'][2]['name']
            tracker_3_value = data_json['legends']['selected']['data'][2]['value']
        

        db.execute("insert into players (name, rank, rankDiv, level, platform, uid, legend, frame, pose, badge1, badge2, badge3, tracker_name1, tracker_name2, tracker_name3, tracker_value1, tracker_value2, tracker_value3) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                data_json['global']['name'],
                data_json['global']['rank']['rankName'],
                data_json['global']['rank']['rankDiv'],
                data_json['global']['level'],
                data_json['global']['platform'],
                data_json['global']['uid'],
                data_json['legends']['selected']['LegendName'],
                data_json['legends']['selected']['gameInfo']['frame'], 
                data_json['legends']['selected']['gameInfo']['pose'],
                data_json['legends']['selected']['gameInfo']['badges'][0]['name'],
                data_json['legends']['selected']['gameInfo']['badges'][1]['name'],
                data_json['legends']['selected']['gameInfo']['badges'][2]['name'],
                tracker_1_name,
                tracker_2_name,
                tracker_3_name,
                tracker_1_value,
                tracker_2_value,
                tracker_3_value
                )
        
            
        history_data = db.execute("SELECT timeCreated, rank, rankDiv, tracker_name1, tracker_name2, tracker_name3, tracker_value1, tracker_value2, tracker_value3 from players WHERE name = ?;", data_json['global']['name'])
    

        
        return render_template("player.html", player_data=data_json, history=history_data)

def lookup(player_id, platform_id):
    url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player_id}&platform={platform_id}"
    print(url)
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)
    return data


