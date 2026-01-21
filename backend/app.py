from flask import Flask
from routes import register_student

app = Flask(__name__)

app.add_url_rule(
    "/register",
    "register",
    register_student,
    methods=["POST"]
)

if __name__ == "__main__":
    app.run(debug=True)
