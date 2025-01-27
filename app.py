from flask import Flask
from blueprints.Homepage import homepage

app = Flask(__name__)

app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run()