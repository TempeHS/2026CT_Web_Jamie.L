from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Mantis Lords", "The three sisters and leaders of the mantis tribe", "Go to boss", "static/images/Card_1.png"),
        ("Nightmare King Grim", "Leader of the grim troupe, and taken over by the nightmare heart", "Go to boss" ),
        ("Sly", "Scammer, Shopkeeper and nail art master", "Go to boss" ),
        ("Gorb", "THE GREAT MIND GORB", "Go to boss"),
    )
    
    return render_template("index.html", cards=card_data), 200


if __name__ == '__main__':
    app.run(debug=True)
``