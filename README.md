# 🎓 学生成绩管理系统

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)

一个基于 Flask 的学生成绩管理系统，提供学生信息管理、成绩统计分析和数据可视化功能。

## ✨ 功能特性

- 学生信息的添加、删除和批量导入
- 成绩统计分析（平均分、最高分、最低分、分差）
- 数据可视化展示
- 数据重置与恢复功能
- 支持 CSV 文件导入导出

## 🚀 快速开始

### 前提条件

- Python 3.8+
- MySQL 8.0+
- Git

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

### 2. 创建并激活虚拟环境
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```
### 3. 安装依赖
```bash
pip install -r requirements.txt
```
### 4. 创建并配置 .env 文件
```bash
# 复制示例文件
cp .env.example .env

## 编辑 .env 文件，配置数据库连接信息
nano .env  # 或使用你喜欢的编辑器
```
  .env 文件内容示例：

```ini
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_strong_password
DB_NAME=student_system
```
### 5. 初始化数据库
```bash
python init_db.py
```
### 6. 运行应用
```bash
python app.py
```
访问 http://localhost:6500 使用系统

🔧 项目结构
```
root/
├── app.py                 # 应用入口
|── config.py              # 数据库配置模块（无敏感信息）
├── init_db.py             # 数据库初始化脚本
├── requirements.txt       # 依赖列表
├── .env.example           # 环境变量(数据库)（示例）
├── .gitignore             # Git忽略规则
├── README.md              # 项目文档
│
├── controllers/           # 控制器
│   └── student_controller.py
│
├── models/                # 数据模型
│   ├── database.py        #数据库操作
│   ├── student.py         #Student模型
│
├── services/              # 服务层，放业务逻辑
│   ├── student_service.py
│   └── stats_service.py
│
└── templates/             # 前端模板
    └── index.html
```
📊 技术栈

后端: Python, Flask

数据库: MySQL

前端: Bootstrap,HTML5

依赖管理: pip,pipreqs 

环境管理: python-dotenv,

📝 使用指南
添加学生:

在"添加新学生"表单中填写学生信息

成绩范围: 0-100分

批量导入:

准备CSV文件，格式: 姓名,班级,语文,数学,英语,计算机

拖拽或选择文件上传

数据分析:

查看各科平均分、最高分、最低分

查看总分统计

数据管理:

删除单个学生记录

清空所有数据并恢复示例

🤝 贡献指南
欢迎提交 Issue 和 Pull Request!

Fork 项目

创建新分支 (git checkout -b feature/your-feature)

提交更改 (git commit -am 'Add some feature')

推送分支 (git push origin feature/your-feature)

创建 Pull Request

📄 许可证
本项目采用 MIT 许可证

数据库配置
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_strong_password
DB_NAME=student_system

可选配置
DEBUG=True
PORT=6500
