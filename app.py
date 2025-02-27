from flask import Flask
from flask_cors import CORS

from blueprints.Homepage import homepage

app = Flask(__name__)
CORS(app)  # 允许所有来源进行跨域请求,否则浏览器会阻止后端到前端的数据传输

app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run(debug=True)