from flask import request, Blueprint
from models import Homepage

homepage = Blueprint('homepage', __name__, url_prefix="/Homepage")

# 格式如下: 127.0.0.1/Homepage/getData?name=xxx
@homepage.route('/getData', strict_slashes=False, methods=['GET', 'POST'])
def get_data():
    id = request.args.get('id')
    name = request.args.get('name')
    # print(f"trying to get data of '{name}'")  # 这个print是用来调试的,会在运行app.py的终端中显示
    response = Homepage.get_data(id)
    # print("response is:",response)
    return response

# 谨慎使用，这个真的能删除数据
@homepage.route('/deleteData', strict_slashes=False, methods=['GET', 'POST'])
def delete_data():
    id = request.args.get('id')
    name = request.args.get('name')
    response = Homepage.delete_data(id)
    return response

@homepage.route('/createData', strict_slashes=False, methods=['GET', 'POST'])
def create_data():
    name = request.args.get('name')
    response = Homepage.create_data(name)
    return response

# 重命名
@homepage.route('/renameData', strict_slashes=False, methods=['GET', 'POST'])
def rename_data():
    id = request.args.get('id')
    newname = request.args.get('newname')
    response = Homepage.rename_data(id,newname)
    return response

# 获取所有数据的条目，因为数据量还不是很大，所以把data的内容也一并传回
@homepage.route('/getDataList', strict_slashes=False, methods=['GET', 'POST'])
def get_data_list():
    response = Homepage.get_data_list()
    return response