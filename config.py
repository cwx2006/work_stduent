#数据库配置
# config.py
import os
import pymysql.cursors
from dotenv import load_dotenv

# 尝试从 .env 文件加载环境变量
if not load_dotenv():
    print("警告: 未找到 .env 文件，将使用系统环境变量")

# 获取配置，如果缺失则报错
def get_env(key, default=None):
    value = os.getenv(key, default)
    if value is None:
        raise EnvironmentError(f"缺少必要的环境变量: {key}")
    return value

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'student_system'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}