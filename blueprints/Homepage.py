from flask import request, Blueprint
from models import Homepage

homepage = Blueprint('homepage', __name__, url_prefix="/Homepage")

# 格式如下: 127.0.0.1/Homepage/getFile?name=xxx
@homepage.route('/getFile', strict_slashes=False, methods=['GET', 'POST'])
def get_file():
    id = request.args.get('id')
    name = request.args.get('name')
    # print(f"trying to get File of '{name}'")  # 这个print是用来调试的,会在运行app.py的终端中显示
    response = Homepage.get_file(id)
    # print("response is:",response)
    return response

# 谨慎使用，这个真的能删除数据
@homepage.route('/deleteFile', strict_slashes=False, methods=['GET', 'POST'])
def delete_file():
    id = request.args.get('id')
    name = request.args.get('name')
    response = Homepage.delete_file(id)
    return response

@homepage.route('/createFile', strict_slashes=False, methods=['GET', 'POST'])
def create_file():
    # name = request.args.get('name')
    response = Homepage.create_file()
    return response

# 重命名
@homepage.route('/renameFile', strict_slashes=False, methods=['GET', 'POST'])
def rename_file():
    id = request.args.get('id')
    newname = request.args.get('newname')
    response = Homepage.rename_file(id,newname)
    return response

# 获取所有数据的条目，因为数据量还不是很大，所以把File的内容也一并传回
@homepage.route('/getFileList', strict_slashes=False, methods=['GET', 'POST'])
def get_file_list():
    response = Homepage.get_file_list()
    return response

@homepage.route('/addComponent', strict_slashes=False, methods=['GET', 'POST'])
def add_component():
    f_id = request.args.get('f_id')  # f即为file
    c_id = request.args.get('c_id')  # c即为component
    c_name = request.args.get('c_name')
    c_type = request.args.get('c_type')
    response = Homepage.add_component(f_id,c_id,c_name,c_type)
    return response

@homepage.route('/changeBatteryStorageParam', strict_slashes=False, methods=['GET', 'POST'])
def change_battery_storage_param():
    f_id = request.args.get('f_id')
    c_id = request.args.get('c_id')
    rated_voltage = request.args.get('rated_voltage')
    capacity = request.args.get('capacity')
    resistance = request.args.get('resistance')
    response = Homepage.change_battery_storage_param(f_id,c_id,rated_voltage,capacity,resistance)
    return response

@homepage.route('/changeWindParam', strict_slashes=False, methods=['GET', 'POST'])
def change_wind_param():
    f_id = request.args.get('f_id')
    c_id = request.args.get('c_id')
    rated_power = request.args.get('rated_power')
    cutin_speed = request.args.get('cutin_speed')
    cutout_speed = request.args.get('cutout_speed')
    response = Homepage.change_wind_param(f_id, c_id, rated_power, cutin_speed, cutout_speed)
    return response

@homepage.route('/changeSolarParam', strict_slashes=False, methods=['GET', 'POST'])
def change_solar_param():
    f_id = request.args.get('f_id')
    c_id = request.args.get('c_id')
    peak_power = request.args.get('peak_power')
    efficiency = request.args.get('efficiency')
    open_voltage = request.args.get('open_voltage')
    response = Homepage.change_solar_param(f_id, c_id, peak_power, efficiency, open_voltage)
    return response

@homepage.route('/deleteComponent', strict_slashes=False, methods=['GET', 'POST'])
def delete_component():
    f_id = request.args.get('f_id')
    c_id = request.args.get('c_id')
    response = Homepage.delete_component(f_id, c_id)
    return response