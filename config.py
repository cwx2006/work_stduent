#数据库配置
# config.py
import os
import pymysql.cursors
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'student_system'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}