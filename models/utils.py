## 这部分是一些小工具，包括数据库操作等。
## 并不是我写的
import pymysql
from dbutils.pooled_db import PooledDB

class DB(object):

    pool = PooledDB(
        pymysql,
        mincached=2,
        maxcached=None,
        maxconnections=None,
        blocking=True,
        user='root',
        password='123456',  # 建议不要改成自己的密码，就用这个
        db='EEEIC',
        host='localhost',
        port=3306,
        charset='utf8')

    # 对创建新表格操作的封装
    @classmethod
    def create(cls, sql):
        conn = cls.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            return 'success'
        except Exception as e:
            print('Exception occurred when creating table:', e)
            conn.rollback()
            return 'error'
        finally:
            conn.close()

    # 对查询数据操作的封装, decorate表示与查询有关的语句（在查询之前执行）
    @classmethod
    def query(cls, sql, decorate=None):
        conn = cls.pool.connection()
        try:
            with conn.cursor() as cursor:
                if decorate:
                    cursor.execute(decorate)
                cursor.execute(sql)
                data = cursor.fetchall()
            return data
        except Exception as e:
            print('Exception occurred when fetching data:', e)
            conn.rollback()
            return None
        finally:
            conn.close()

    # 对增加数据操作的封装
    @classmethod
    def insert(cls, sql, data):
        '''
        :param data: tuple
        '''
        conn = cls.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, data)
            conn.commit()
            return 'success'
        except Exception as e:
            print('Exception occurred when inserting data:', e)
            conn.rollback()
            return 'error'
        finally:
            conn.close()

    # 对更新数据操作的封装
    @classmethod
    def update(cls, sql):
        '''
        :param data: tuple
        '''
        conn = cls.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            return 'success'
        except Exception as e:
            print('Exception occurred when inserting data:', e)
            conn.rollback()
            return 'error'
        finally:
            conn.close()

    # 对删除数据操作的封装
    @classmethod
    def delete(cls, sql):
        '''
        :param data: tuple
        '''
        conn = cls.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            return 'success'
        except Exception as e:
            print('Exception occurred when deleting data:', e)
            conn.rollback()
            return 'error'
        finally:
            conn.close()
