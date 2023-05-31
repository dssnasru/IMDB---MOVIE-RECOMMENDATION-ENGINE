from flask import Flask , render_template , request
from model import movies,database


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("home.html")


@app.route("/result", methods=["POST","GET"])
def res():
    if request.method == "POST":
        nme = request.form["nme"]
        x=movies(nme.lower())
        if x == 1:
            return render_template("error.html",ans = nme)

        return render_template("results.html",ans = x)
    return render_template("results.html")


@app.route("/database")
def db():
    x = database()
    return render_template("database.html",ans = x)

if __name__ == "__main__":
    app.run(debug=True)