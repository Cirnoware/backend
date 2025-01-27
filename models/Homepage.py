from models.utils import DB
from flask import jsonify

def get_data(name):
    # 这部分的代码参考服务器端的代码，在EEEIC/Meter/backend/中
    # 这个代码可能会有SQL注入的问题，请不要尝试攻击
    sql = f"SELECT data FROM home WHERE name = '{name}';"    # 使用f-string格式化字符串
    response = DB.query(sql)
    return jsonify(response)    # 必须要json一下

def delete_data(name):
    sql = f"DELETE FROM home WHERE name = '{name}';"
    response = DB.delete(sql)
    return jsonify(response)    # 必须要json一下