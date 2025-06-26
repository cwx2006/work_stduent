# models/database.py
import pymysql

from config import DB_CONFIG


class DBManager:
    def __init__(self, config=DB_CONFIG):
        self.config = config # 数据库连接信息
        self.init_database()

    def get_connection(self):#连接
        return pymysql.connect(**self.config)

    def init_database(self):
        try:
            create_db_config = self.config.copy()
            create_db_config.pop('database')

            with pymysql.connect(**create_db_config) as conn:#
                with conn.cursor() as cursor:#尽量大写,使用utf8mb4支持所有Unicode字符
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.config['database']} DEFAULT CHARSET utf8mb4")

            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""  
                    CREATE TABLE IF NOT EXISTS students (
                        id INT AUTO_INCREMENT PRIMARY KEY, --  id  自增主键
                        `name` VARCHAR(50) NOT NULL, -- 中文、英文姓名 MySQL保留字用反引号包裹
                        classes VARCHAR(50) not NULL DEFAULT "", -- 
                        cn DECIMAL(5,2)  unsigned, -- 语文   使用DECIMAL  5位数字含2位小数
                        `math`  DECIMAL(5,2) unsigned, -- 数学成绩
                        eng  DECIMAL(5,2) unsigned, -- 英语成绩
                        cs DECIMAL(5,2) unsigned, -- 计算机成绩 
                        total_score DECIMAL(5,2) DEFAULT 0 -- 默认0  
                    )comment='学生信息表';   -- 不用在外面定义
                    """)
                    conn.commit()
        except Exception as e:
            print(f"数据库初始化失败: {str(e)}")

    def get_all_students(self):
        students = []
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT name, classes, cn, math, eng, cs FROM students")
                    for row in cursor.fetchall():
                        students.append(row)
        except Exception as e:
            print(f"从数据库读取学生失败: {str(e)}")
        return students

    def add_student(self, name, classes, cn, math, eng, cs):
        try:
            total_score = cn + math + eng + cs
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                    INSERT INTO students (name, classes, cn, math, eng, cs, total_score)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (name, classes, cn, math, eng, cs, total_score))
                    conn.commit()
            return True
        except pymysql.Error as e:
            print(f"数据库错误: {e.args[0]} - {e.args[1]}")
            return False
        except Exception as e:
            print(f"添加学生到数据库失败: {str(e)}")
            return False
    def import_students(self, students_data):
        try:
            values = []
            for s in students_data:
                total_score = s['cn'] + s['math'] + s['eng'] + s['cs']
                values.append((
                    s['name'], s['classes'],
                    s['cn'], s['math'], s['eng'], s['cs'], total_score
                ))

            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.executemany("""
                    INSERT INTO students (name, classes, cn, math, eng, cs, total_score)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, values)
                    conn.commit()
            return True
        except Exception as e:
            print(f"批量导入学生失败: {str(e)}")
            return False

    def delete_student(self, name, classes):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                    DELETE FROM students 
                    WHERE name = %s AND classes = %s  -- 匹配,and 防止误删同名不同班的学生
                    """, (name, classes))
                    conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"删除学生失败: {str(e)}")
            return False

    def clear_data(self):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("TRUNCATE TABLE students")
                    examples = [
                        ("张三", "一班", 85, 92, 78, 90),
                        ("李四", "二班", 78, 88, 85, 92)
                    ]
                    for data in examples:
                        total = sum(data[2:])
                        cursor.execute("""
                        INSERT INTO students (name, classes, cn, math, eng, cs, total_score)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)  -- 添加%s防止SQL注入
                        """, (*data, total))
                    conn.commit()
            return True
        except Exception as e:
            print(f"重置数据库失败: {str(e)}")
            return False