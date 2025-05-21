from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Mantis Lords", "The Mantis Lords are 3 sisters you must fight and defeat in the Mantis Village", "Go to boss", "static/images/Card_1"),
        ("Nightmare King Grim", "Leader of the grim troupe, and taken over by the nightmare heart", "Go to boss", )
    )
    
    return render_template("index.html", cards=card_data), 200


if __name__ == '__main__':
    app.run(debug=True)
