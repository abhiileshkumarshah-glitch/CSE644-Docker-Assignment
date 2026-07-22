from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>CSE644 Cloud Computing</h1>
        <h2>Python Flask Docker Web Server</h2>
        <p>Student: Abhi Shah</p>
        <p>Running inside Docker on port 8888</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)