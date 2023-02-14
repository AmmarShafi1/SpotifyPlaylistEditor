from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import shuffler

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    if request.method == "POST":
        return redirect(url_for('user'))
    return render_template("index.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session.permanent = True
#         user = request.form["nm"]
#         session["user"] = user
#         return redirect(url_for('user'))
#     else:
#         if "user" in session:
#             return redirect(url_for("user"))
#         return render_template("login.html")


# @app.route("/user")
# def user():
#     if "user" in session:
#         user = session["user"]
#         return redirect(url_for("shuffleSelect"))
#     else:
#         return redirect(url_for("login"))


# @app.route("/enterplname", methods=["POST", "GET"])
# def enterplname():
#     if request.method == "POST":
#         plnm = request.form["pln"]
#         shuffler.newShufflePl(plnm)
#         # subprocess.run(['python','/Users/ammar/PycharmProjects/SpotifyShuffler/shf.py',plnm])
#         return render_template("shuffling.html")
#     else:
#         return render_template("enterPlName.html")


@app.route('/<pName>/<newPL>/shuffling', methods=['GET', 'POST'])
def shuffling(pName, newPL):
    if newPL == "2":
        pID = shuffler.oldShufflePl(pName)
        return redirect(url_for('doneshuffling', pID=pID))
    if newPL == "3":
        pID = shuffler.newShufflePl(pName)
        return redirect(url_for('doneshuffling', pID=pID))



@app.route("/<pID>/doneshuffling", methods=['GET', 'POST'])
def doneshuffling(pID):
    pInfo = shuffler.plInfo(pID)
    pName = pInfo[0]
    pLink = pInfo[1]
    pImage = pInfo[2]
    return render_template("doneshuffling.html", pName=pName, pImage=pImage, pLink=pLink)

@app.route("/<pID>/donecombining", methods=['GET', 'POST'])
def donecombining(pID):
    pInfo = shuffler.plInfo(pID)
    pName = pInfo[0]
    pLink = pInfo[1]
    pImage = pInfo[2]
    return render_template("donecombining.html", pName=pName, pImage=pImage, pLink=pLink)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# @app.route("/shuffleSelect", methods=["GET", "POST"])
# def shuffleSelect():
#     if request.method == "POST":
#         if (request.form.getlist('check')) == ["Create New Playlist"]:
#             return redirect(url_for('shuffleSelectNew'))
#     images = shuffler.labeledPlaySet()
#     return render_template("shuffleSelect.html", images=images)


# @app.route("/shuffleSelectNew", methods=["GET", "POST"])
# def shuffleSelectNew():
#     if request.method == "POST":
#         if (request.form.getlist('check')) == ["Shuffle Original Playlist"]:
#             redirect(url_for('shuffleSelect'))
#     images = shuffler.labeledPlaySet()
#     return render_template("shuffleSelectNew.html", images=images)

@app.route("/combinePl", methods=['GET','POST'])
def combinePl():
    images = shuffler.labeledPlaySet()
    if request.method == "POST":
        newPlName = request.form.get('newPlName')
        tempNums = request.form.getlist('plcom')
        if not tempNums or not newPlName:
            return render_template('combinePl.html', images=images)
        pNums = [eval(i) for i in tempNums]
        shuffler.combinePl(pNums, newPlName)
        pID = shuffler.get_play_id(newPlName)
        return redirect(url_for('donecombining', pID=pID))

    return render_template('combinePl.html', images=images)


@app.route("/shufflePl", methods=["GET", "POST"])
def shufflePl():
    if request.method == "POST":
        pName = request.form.get('pl')
        if (request.form.getlist('check')) == ["Shuffle Original Playlist"]:
            return redirect(url_for('shuffling',pName = pName,newPL = 2 ))
        elif (request.form.getlist('check')) == ["Create New Playlist"]:
            return redirect(url_for('shuffling',pName = pName,newPL = 3 ))
    images = shuffler.labeledPlaySet()
    return render_template('shufflePl.html', images = images)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
