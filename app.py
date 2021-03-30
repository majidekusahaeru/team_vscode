from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/kyuryou")
def kyuryou():
    return render_template("kyuryou.html")
@app.route("/kyuryou_re")
def kyuryou_re():
    ji = request.args.get("ji")
    ro = request.args.get("ro")
    re = ji * ro
    return render_template("kyuryou_re.html",re= re)

@app.route("/enkeisan")
def enkeisan():
    return render_template("keisan1.html")

@app.route("/keisan")
def keisan():
    hankei= int(request.args.get("hankei"))
    p = 314
    syu = hankei * 2 * p /100
    men = hankei * hankei * p /100
    return render_template("hantei.html",syu = syu,men = men)

if __name__ == "__main__":

    app.run(debug=True)