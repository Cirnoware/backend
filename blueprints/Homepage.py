from flask import request, Blueprint
from models import Homepage

homepage = Blueprint('homepage', __name__, url_prefix="/Homepage")

# 格式如下: 127.0.0.1/Homepage/getFile?name=xxx

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

@homepage.route('/getFile', strict_slashes=False, methods=['GET', 'POST'])
def get_file():
    f_id = request.args.get('f_id')
    response = Homepage.get_file(f_id)
    return response

@homepage.route('/getDeviceList', strict_slashes=False, methods=['GET', 'POST'])
def get_device_list():
    f_id = request.args.get('f_id')
    response = Homepage.get_device_list(f_id)
    return response

@homepage.route('/addDevice', strict_slashes=False, methods=['GET', 'POST'])
def add_device():
    f_id = request.args.get('f_id')  # f即为file
    d_id = request.args.get('d_id')  # c即为device
    d_name = request.args.get('d_name')
    d_dispname = request.args.get('d_dispname')
    d_type = request.args.get('d_type')
    x = request.args.get('x')
    y = request.args.get('y')
    response = Homepage.add_device(f_id,d_id,d_name,d_dispname,d_type,x,y)
    return response

@homepage.route('/changeBatteryParam', strict_slashes=False, methods=['GET', 'POST'])
def change_battery_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    Pload1 = request.args.get('Pload1')
    Cload1 = request.args.get('Cload1')
    response = Homepage.change_battery_param(f_id,d_id,Pload1,Cload1)
    return response

@homepage.route('/changeWindParam', strict_slashes=False, methods=['GET', 'POST'])
def change_wind_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    Pload1 = request.args.get('Pload1')
    Cload1 = request.args.get('Cload1')
    response = Homepage.change_wind_param(f_id, d_id, Pload1, Cload1)
    return response

@homepage.route('/changeSolarParam', strict_slashes=False, methods=['GET', 'POST'])
def change_solar_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    Pload1 = request.args.get('Pload1')
    Cload1 = request.args.get('Cload1')
    response = Homepage.change_solar_param(f_id, d_id, Pload1, Cload1)
    return response

@homepage.route('/changeGridParam', strict_slashes=False, methods=['GET', 'POST'])
def change_grid_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    fo = request.args.get('fo')
    Vgabc0 = request.args.get('Vgabc0')
    Lf = request.args.get('Lf')
    Rf = request.args.get('Rf')
    Lg = request.args.get('Lg')
    Rg = request.args.get('Rg')
    response = Homepage.change_grid_param(f_id, d_id, fo, Vgabc0, Lf, Rf, Lg, Rg)
    return response

@homepage.route('/changeVSCParam', strict_slashes=False, methods=['GET', 'POST'])
def change_vsc_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    fs = request.args.get('fs')
    Kip = request.args.get('Kip')
    Kii = request.args.get('Kii')
    Kvp = request.args.get('Kvp')
    Kvi = request.args.get('Kvi')
    Kpllp = request.args.get('Kpllp')
    Kplli = request.args.get('Kplli')
    Td = request.args.get('Td')
    Ktp = request.args.get('Ktp')
    Kti = request.args.get('Kti')
    response = Homepage.change_vsc_param(f_id, d_id, fs, Kip, Kii, Kvp, Kvi, Kpllp, Kplli, Td, Ktp, Kti)
    return response

@homepage.route('/changeBusParam', strict_slashes=False, methods=['GET', 'POST'])
def change_bus_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    Vdc0 = request.args.get('Vdc0')
    Cdc = request.args.get('Cdc')
    response = Homepage.change_bus_param(f_id, d_id, Vdc0, Cdc)
    return response

@homepage.route('/changeLoadParam', strict_slashes=False, methods=['GET', 'POST'])
def change_load_param():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    Pload1 = request.args.get('Pload1')
    Cload1 = request.args.get('Cload1')
    response = Homepage.change_load_param(f_id, d_id, Pload1, Cload1)
    return response

@homepage.route('/deleteDevice', strict_slashes=False, methods=['GET', 'POST'])
def delete_device():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    response = Homepage.delete_device(f_id, d_id)
    return response

@homepage.route('/addWire', strict_slashes=False, methods=['GET', 'POST'])
def add_wire():
    f_id = request.args.get('f_id')
    w_id = request.args.get('w_id')
    start_d = request.args.get('start_d')
    end_d = request.args.get('end_d')
    start_side = request.args.get('start_side')
    end_side = request.args.get('end_side')
    response = Homepage.add_wire(f_id, w_id,start_d, end_d,start_side,end_side)
    return response

@homepage.route('/changeWireParam', strict_slashes=False, methods=['GET', 'POST'])
def change_wire_param():
    f_id = request.args.get('f_id')
    w_id = request.args.get('w_id')
    resistance = request.args.get('resistance')
    inductance = request.args.get('inductance')
    response = Homepage.change_wire_param(f_id, w_id, resistance, inductance)
    return response

@homepage.route('/changeDevicePos', strict_slashes=False, methods=['GET', 'POST'])
def change_device_pos():
    f_id = request.args.get('f_id')
    d_id = request.args.get('d_id')
    x = request.args.get('x')
    y = request.args.get('y')
    response = Homepage.change_device_pos(f_id, d_id, x, y)
    return response