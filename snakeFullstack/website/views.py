from flask import Blueprint, render_template, request
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        i1 = request.form.get("i1")
        i2 = request.form.get("i2")
        i3 = request.form.get("i3")
        score = request.form.get("score")
        with open("./leaderboard.json", 'r+') as file:
            newdata = {}
            data = json.loads(file.read())
            data[101] = {"score": score, "name": (i1+i2+i3) }
            sorted_items = sorted(data.items(), reverse=True, key=lambda item: int(item[1]["score"]))
            for counter, (key, value) in enumerate(sorted_items[0:50]):
                newdata[str(counter+1)] = value
            print(newdata)
            #printing
            file.seek(0)
            file.truncate()
            file.write(json.dumps(newdata))

    return render_template("snake.html") #this is where you pass in jinja 2 vars


@views.route("/leaderboard")
def leaderboard():
    with open("./leaderboard.json", "r") as file:
        _leaderboard = json.loads(file.read()).items()

    print(_leaderboard)

    return render_template("leaderBoard.html", leaderboard=_leaderboard) #this is where you pass in jinja 2 vars