from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

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