from flask import Flask, render_template, request, redirect
import requests
import json


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def findPlayer():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form.get("player_id")
        platform = request.form.get("platform")


        if not username:
            print("Sorry, need username or username not found")

        if not platform:
            print("Sorry, need platform or platform not found")
            print("use PSN, XBL, Steam, Origin")


        data = lookup(username, platform)
        print(data)

        # lookup(username, platform)






        return render_template("playerFound.html")

def lookup(player_id, platform_id):

    API_KEY = "9e62c7230a4e7afe9e409b010f663bb5"
    url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player=PikaPlayzMC3083&platform=X1"
    print(url)
    response = requests.get(url)
    data = response.json()
    return data
