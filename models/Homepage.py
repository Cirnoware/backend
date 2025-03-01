from models.utils import DB
from flask import jsonify
from datetime import datetime
import os,json



def delete_file(id):
    sql = f"DELETE FROM home WHERE id = '{id}';"
    response = DB.delete(sql)
    return jsonify(response)    # 必须要json一下

def create_file():  # 只生成id，不设置名称
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    id = current_time.strftime('%Y%m%d%H%M%S')  # 为避免重复，id为创建数据时的时间
    print(id)

    # 生成默认的仿真文件内容
    base_dir = os.path.dirname(__file__)  # 获取 B.py 所在目录
    file_path = os.path.join(base_dir, "..\\src", "defaultFile.json")  # 拼接出 D.json 的路径
    with open(file_path, 'r') as f:
        DEFAULT_FILE = f.read()
    data = DEFAULT_FILE

    # 将结果写入数据库
    sql = f"INSERT INTO `eeeic`.`home` (`id`, `data`, `create_time`) VALUES ('{id}', '{data}', '{formatted_time}')"
    DB.create(sql)
    return jsonify({"id": id})

def rename_file(id,newname):
    sql = f"UPDATE eeeic.home SET name = '{newname}' WHERE id = '{id}'"
    response = DB.update(sql)
    return jsonify(response)

def get_file_list():
    sql = "SELECT id, name FROM eeeic.home;"
    response = DB.query(sql)
    formatted_response = [{'id': row[0], 'name': row[1]} for row in response] 
    return jsonify(formatted_response)

def get_file(f_id):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    return jsonify(f_data)

def get_device_list(f_id):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    # print(f_data["devices"])
    return jsonify(f_data["devices"])

def add_device(f_id,d_id,d_name,d_dispname,d_type,x,y):
    # print(f_id,d_id,d_name,d_type)
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    f_data["system_info"]["device_count_total"] += 1
    new_data = ""
    if (d_type == 'Battery'):
        f_data["system_info"]["battery_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["battery_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "capacity": 1000,
                "rated_voltage": 500,
                "resistance": 0.95
            }
        }  
    elif (d_type == 'Wind'):
        f_data["system_info"]["wind_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["wind_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "rated_power": 1000,
                "cutin_speed": 3,
                "cutout_speed": 25
            },
        }
        
    elif (d_type == 'Solar'):
        f_data["system_info"]["solar_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["solar_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "rated_power": 1000,
                "efficiency": 0.2,
                "open_voltage": 500
            }
        }
    elif (d_type == 'Grid'):
        f_data["system_info"]["grid_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["grid_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "f0": 50,
                "Vgabc0": 380,
                "Lf": 3.65e-3,
                "Rf": 0.01,
                "Lg": 2.5e-3,
                "Rg": 0.15
            }
        }
    elif (d_type == 'VSC'):
        f_data["system_info"]["vsc_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["vsc_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "fs": 5e3,
                "Kip": 5,
                "Kii": 500,
                "Kvp": 0.35,
                "Kvi": 20,
                "Kpllp": 5,
                "Kplli": 50,
                "Td": 200e-6,
                "Ktp": 0.1,
                "Kti": 50
            }
        }
    elif (d_type == 'Bus'):
        f_data["system_info"]["bus_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["bus_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "Vdc0": 700,
                "Cdc": 1500e-6
            }
        }
    elif (d_type == 'Load'):
        f_data["system_info"]["load_count"] += 1
        d_data = {
            "d_id": f"{d_id}",
            "d_type": f"{d_type}",
            "d_name": f"{d_name}",
            "d_dispname": f"{d_dispname}{f_data["system_info"]["load_count"]}",
            "x": x,
            "y": y,
            "parameters": {
                "Pload1": 10e3,
                "Cload1": 200e-6
            }
        }
    f_data["devices"].append(d_data)
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    # print(new_data)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    # print(response)
    return jsonify(response)

def change_battery_param(f_id,d_id,rated_voltage,capacity,resistance):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["capacity"] = capacity
            device["parameters"]["rated_voltage"] = rated_voltage
            device["parameters"]["resistance"] = resistance
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_wind_param(f_id,d_id,rated_power,cutin_speed,cutout_speed):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["rated_power"] = rated_power
            device["parameters"]["cutin_speed"] = cutin_speed
            device["parameters"]["cutout_speed"] = cutout_speed
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_solar_param(f_id,d_id,rated_power,efficiency,open_voltage):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["rated_power"] = rated_power
            device["parameters"]["efficiency"] = efficiency
            device["parameters"]["open_voltage"] = open_voltage
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_grid_param(f_id, d_id, f0, Vgabc0, Lf, Rf, Lg, Rg):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["f0"] = f0
            device["parameters"]["Vgabc0"] = Vgabc0
            device["parameters"]["Lf"] = Lf
            device["parameters"]["Rf"] = Rf
            device["parameters"]["Lg"] = Lg
            device["parameters"]["Rg"] = Rg
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_vsc_param(f_id, d_id, fs, Kip, Kii, Kvp, Kvi, Kpllp, Kplli, Td, Ktp, Kti):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["fs"] = fs
            device["parameters"]["Kip"] = Kip
            device["parameters"]["Kii"] = Kii
            device["parameters"]["Kvp"] = Kvp
            device["parameters"]["Kvi"] = Kvi
            device["parameters"]["Kpllp"] = Kpllp
            device["parameters"]["Kplli"] = Kplli
            device["parameters"]["Td"] = Td
            device["parameters"]["Ktp"] = Ktp
            device["parameters"]["Kti"] = Kti
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_load_param(f_id, d_id, Pload1, Cload1):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["Pload1"] = Pload1
            device["parameters"]["Cload1"] = Cload1
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_bus_param(f_id, d_id, Vdc0, Cdc):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["parameters"]["Vdc0"] = Vdc0
            device["parameters"]["Cdc"] = Cdc
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def delete_device(f_id,d_id):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            f_data["devices"].remove(device)
            break
    # 删除相连的导线
    for wire in f_data["wires"]:
        if wire["start_d"] == d_id or wire["end_d"] == d_id:
            f_data["wires"].remove(wire)
            f_data["system_info"]["wire_count"] -= 1
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def add_wire(f_id, w_id,start_d,end_d,start_side,end_side):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    f_data["system_info"]["wire_count"] += 1
    # wire_data = {
    #     "w_id": f"{w_id}",
    #     "start": {"x": start_x, "y": start_y},
    #     "end": {"x": end_x, "y": end_y}
    # }
    wire_data = {
        "w_id": f"{w_id}",
        "start_d": f"{start_d}",
        "start_side": f"{start_side}",
        "end_d": f"{end_d}",
        "end_side": f"{end_side}",
        "parameters": {
            "resistance": 0.3,
            "inductance": 0.001
        }
    }
    if "wires" not in f_data:
        f_data["wires"] = []
    f_data["wires"].append(wire_data)
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_wire_param(f_id,w_id,resistance,inductance):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for wire in f_data["wires"]:
        if wire["w_id"] == w_id:
            wire["parameters"]["resistance"] = resistance
            wire["parameters"]["inductance"] = inductance
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)

def change_device_pos(f_id, d_id, x, y):
    sql = f"SELECT data FROM eeeic.home WHERE id = '{f_id}';"
    f_data = DB.query(sql)
    f_data = json.loads(f_data[0][0])
    for device in f_data["devices"]:
        if device["d_id"] == d_id:
            device["x"] = x
            device["y"] = y
            break
    new_data = json.dumps(f_data, indent=4, ensure_ascii=False)
    sql = f"UPDATE eeeic.home SET data = '{new_data}' WHERE id = '{f_id}';"
    response = DB.update(sql)
    return jsonify(response)