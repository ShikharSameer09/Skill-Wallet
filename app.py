from flask import Flask, render_template, request

app = Flask(__name__)

def ai_recommend(room, style, color):

    if style == "Modern":
        return f"A modern {room} with {color} theme and smart lighting."

    if style == "Traditional":
        return f"A traditional {room} with wooden furniture and {color} colors."

    return f"A minimalist {room} with soft {color} tones."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    room = request.form["room"]
    style = request.form["style"]
    color = request.form["color"]

    result = ai_recommend(room, style, color)

    return f"<h2>AI Design Recommendation</h2><p>{result}</p>"


app.run(debug=True)
