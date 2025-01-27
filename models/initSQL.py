## 不要看这个文件，我们现在使用navicat来管理数据库

from models.utils import DB

def create_database():
    sql = '''
    CREATE DATABASE IF NOT EXISTS EEEIC DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
    '''
    return DB.create(sql)

def create_table():
    sql = '''
    CREATE TABLE IF NOT EXISTS EEEIC.Homepage (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT NOT
    );
    '''
    return DB.create(sql)

if __name__ == '__main__':
    sql = '''
    CREATE TABLE IF NOT EXISTS EEEIC.Homepage (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT NOT
    );
    '''
    DB.create(sql)
    create_database()
    create_table()