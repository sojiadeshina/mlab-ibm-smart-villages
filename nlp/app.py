from flask import Flask, render_template
from random import randint
import Watson

Watson.main("")

app = Flask(__name__)

def BLACK_BOX_FUNCTION(query):
    rnd = randint(0,3)
    if rnd == 0:
        return "mu-lambda-beta"
    if rnd == 1:
        return "eye bee em"
    if rnd == 2:
        return "wot in tarnation???"
    if rnd == 3:
        return "sad reacts only"
    return "God save the queen"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    #return BLACK_BOX_FUNCTION(str(query))
    return Watson.main(str(query))

if __name__ == "__main__":
    app.run()

