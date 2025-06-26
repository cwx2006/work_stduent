

结构
FlaskProjectv4/
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── database.py
├── services/
│   ├── __init__.py
│   ├── student_service.py
│   └── stats_service.py
├── controllers/
│   ├── __init__.py
│   └── student_controller.py
├── templates/
│   └── index.html
└── static/



将数据库配置提取到config.py

Student模型独立到models/student.py

数据库操作封装在models/database.py

业务逻辑放在services/目录

路由控制器放在controllers/

使用Blueprint组织路由

保持原有功能不变