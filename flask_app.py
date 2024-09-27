from flask import Flask
from flask import render_template
from flask.helpers import send_file

import SingleEvaluation.SingleEvaluation

app = Flask(__name__)

@app.route("/")
def index():
    # return SingleEvaluation.SingleEvaluation.main()
    return render_template("index.html")

@app.route("/taskpane.html")
def taskpane():
    output = SingleEvaluation.SingleEvaluation.main()
    return render_template("taskpane.html", output=output)

@app.route("/taskpanedev.html")
def taskpanedev():
    output = SingleEvaluation.SingleEvaluation.main()
    return render_template("taskpanedev.html", output=output)

@app.route("/commands.html")
def commands():
    return render_template("commands.html")

@app.route("/assets/icon-16.png")
def icon16():
    return send_file("./static/assets/icon-16.png",mimetype='image/png')

@app.route("/assets/icon-32.png")
def icon32():
    return send_file("./static/assets/icon-32.png",mimetype='image/png')

@app.route("/assets/icon-64.png")
def icon64():
    return send_file("./static/assets/icon-64.png",mimetype='image/png')

@app.route("/assets/icon-80.png")
def icon128():
    return send_file("./static/assets/icon-80.png",mimetype='image/png')

@app.route("/assets/logo-filled.png")
def iconlogofilled():
    return send_file("./static/assets/logo-filled.png",mimetype='image/png')

@app.route('/favicon.ico')
def favicon():
    return send_file('./static/favicon.ico', mimetype='image/vnd.microsoft.icon')
    
if __name__ == "__main__":
    app.run(debug=True)
