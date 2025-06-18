from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Mantis Lords", "The three sisters and leaders of the mantis tribe", "/mantislords.html", "static/images/Card_1.png"),
        ("Nightmare King Grim", "Leader of the grim troupe, and taken over by the nightmare heart", "/bossinfo.html" ),
        ("Sly", "Scammer, Shopkeeper and nail art master", "/bossinfo.html" ),
        ("Gorb", "THE GREAT MIND GORB", "/bossinfo.html"),
        ("Hornet Protector", "Protector of hallownest", "/hornet1.html"),
    )
    
    return render_template("index.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/checklist.html')
def checklist():
    return render_template("checklist.html"), 200

@app.route('/bossinfo.html')
def bossinfo():
    return render_template("bossinfo.html"), 200

@app.route('/falseknight.html')
def falseknight():
    return render_template("falseknight.html"), 200

@app.route('/gruzmother.html')
def gruzmother():
    return render_template("gruzmother.html"), 200

@app.route('/broodingmawlek.html')
def broodingmawlek():
    return render_template("broodingmawlek.html"), 200

@app.route('/hornet1.html')
def hornet1():
    return render_template("hornet1.html"), 200

@app.route('/MMM.html')
def MMM():
    return render_template("MMM.html"), 200

@app.route('/mantislords.html')
def mantislords():
    return render_template("mantislords.html"), 200

@app.route('/soulmaster.html')
def soulmaster():
    return render_template("soulmaster.html"), 200

@app.route('/brokenvessel.html')
def brokenvessel():
    return render_template("brokenvessel.html"), 200

@app.route('/xero.html')
def xero():
    return render_template("xero.html"), 200

@app.route('/scam.html')
def scam():
    return render_template("scam.html"), 200

@app.route('/scam2.html')
def scam2():
    return render_template("scam2.html"), 200

if __name__ == '__main__':
    app.run(debug=True)