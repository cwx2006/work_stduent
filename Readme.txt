

结构
root/
├── .gitignore          # git忽略规则
├── .env                # 本地环境变量（被忽略）
├── requirements.txt    # 依赖列表
├── app.py
├── config.py           # 数据库配置模块（无敏感信息）
├── models/
│   ├── __init__.py
│   ├── student.py      #Student模型
│   └── database.py     #数据库操作
├── services/           #业务逻辑
│   ├── __init__.py
│   ├── student_service.py
│   └── stats_service.py
├── controllers/        #路由控制器
│   ├── __init__.py
│   └── student_controller.py
├── templates/
│   └── index.html
└── static/
