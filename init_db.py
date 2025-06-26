# init_db.py
from models.database import DBManager

if __name__ == '__main__':
    print("正在初始化数据库...")
    try:
        db_manager = DBManager()
        print("✅ 数据库初始化成功!")
        print(f"请运行 'python app.py' 启动应用")
    except Exception as e:
        print(f"❌ 数据库初始化失败: {str(e)}")
        print("请检查以下可能的问题:")
        print("1. 数据库服务是否正在运行")
        print("2. .env 文件中的数据库配置是否正确")
        print("3. 数据库用户是否有足够的权限")