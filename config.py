#数据库配置
import os
import pymysql.cursors
# 从环境变量获取数据库配置，提供默认值
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '15916188538'),
    'database': os.getenv('DB_NAME', 'student_system'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}