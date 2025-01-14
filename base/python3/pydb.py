import pandas as pd
import redis
import json
import sqlite3

# 连接到 Redis 服务器
def connect_to_redis(host='172.31.174.62', port=6379, passwd='0706Test',db=1):
    try:
        r = redis.Redis(host=host, port=port, password=passwd, db=db, decode_responses=True)
        r.ping()  # 测试连接是否成功
        print("Connected to Redis")
        return r
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        return None

def connect_to_sqlite3():
    # 连接到 SQLite 数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('../infra.db')
    return conn
"""
    # 创建一个游标对象
    cursor = conn.cursor()

    # 创建表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    # 插入数据
    users_data = [
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35)
    ]

    cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users_data)

    # 提交事务
    conn.commit()

    # 查询数据
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("用户列表：")
    for row in rows:
        print(row)

    # 更新数据
    cursor.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'Alice'))
    conn.commit()

    # 再次查询数据以确认更新
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("\n更新后的用户列表：")
    for row in rows:
        print(row)

    # 删除数据
    cursor.execute('DELETE FROM users WHERE name = ?', ('Charlie',))
    conn.commit()

    # 再次查询数据以确认删除
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("\n删除后的用户列表：")
    for row in rows:
        print(row)
    return conn
"""

def disconnect_to_sqlite3(conn):
    # 关闭连接
    conn.close()
    return 

def view_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print(df)
    except Exception as e:
        print(f"Error reading the file: {e}")

def write_to_xlsx(file_path, sheet,data):
    # 创建一个 DataFrame
    if data == None :
        data = {
            '姓名': ['张三', '李四', '王五'],
            '年龄': [25, 30, 22],
            '城市': ['北京', '上海', '广州']
        }
    df = pd.DataFrame(data)

    # 将 DataFrame 写入 Excel 文件
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet, index=False)

    print("Excel 文件已成功保存！")

if __name__ == "__main__":
    # # 连接 Redis
    # redis_client = connect_to_redis()
    # if redis_client:
    #    redis_client.set("name", "jackson")
    
    # # 连接sqlite
    # sqlite_client = connect_to_sqlite3()
    # disconnect_to_sqlite3(sqlite_client)

    # # 连接xlsx
    write_to_xlsx(file_path='test.xlsx', data=None)
    view_excel(file_path='test.xlsx')
