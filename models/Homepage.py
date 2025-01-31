from models.utils import DB
from flask import jsonify
from datetime import datetime

def get_data(id):
    # 这部分的代码参考服务器端的代码，在EEEIC/Meter/backend/中
    # 这个代码可能会有SQL注入的问题，请不要尝试攻击
    sql = f"SELECT data FROM home WHERE id = '{id}';"    # 使用f-string格式化字符串
    response = DB.query(sql)
    return jsonify(response)    # 必须要json一下

def delete_data(id):
    sql = f"DELETE FROM home WHERE id = '{id}';"
    response = DB.delete(sql)
    return jsonify(response)    # 必须要json一下

def create_data():  # 只生成id，不设置名称
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    id = current_time.strftime('%Y%m%d%H%M%S')  # 为避免重复，id为创建数据时的时间
    print(id)
    data = 'this is ' + str(id)
    sql = f"INSERT INTO `eeeic`.`home` (`id`, `data`, `create_time`) VALUES ('{id}', '{data}', '{formatted_time}')"
    DB.create(sql)
    return jsonify({"id": id})

def rename_data(id,newname):
    sql = f"UPDATE eeeic.home SET name = '{newname}' WHERE id = '{id}'"
    response = DB.update(sql)
    return jsonify(response)

def get_data_list():
    sql = "SELECT id, name FROM eeeic.home;"
    response = DB.query(sql)
    formatted_response = [{'id': row[0], 'name': row[1]} for row in response] 
    return jsonify(formatted_response)
