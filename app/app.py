from flask import Flask, render_template, request, redirect
import requests
import json


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def findPlayer():
    if request.method == "GET":
        return render_template("index.html")
    else:
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
        return render_template("playerFound.html", player_data=data_json)

def lookup(player_id, platform_id):

    API_KEY = "9e62c7230a4e7afe9e409b010f663bb5"
    url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player_id}&platform={platform_id}"
    print(url)
    response = requests.get(url)
    data = response.json()
    return data
