from flask import request, Blueprint
from models import Homepage

homepage = Blueprint('homepage', __name__, url_prefix="/Homepage")

# 格式如下: 127.0.0.1/Homepage/getData?name=xxx
@homepage.route('/getData', strict_slashes=False, methods=['GET', 'POST'])
def get_data():
    name = request.args.get('name')
    # print(f"trying to get data of '{name}'")  # 这个print是用来调试的,会在运行app.py的终端中显示
    response = Homepage.get_data(name)
    # print("response is:",response)
    return response

# 谨慎使用，这个真的能删除数据
@homepage.route('/deleteData', strict_slashes=False, methods=['GET', 'POST'])
def delete_data():
    name = request.args.get('name')
    response = Homepage.delete_data(name)
    return response