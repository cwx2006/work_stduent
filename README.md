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
git clone https://github.com/cwx2006/work_student.git
cd work_stduen # 打开文件夹
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
### 4. 创建并配置 .env 文件(以Linux系统为例)
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
work_student/
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
### 💻 技术栈

| 类别       | 技术               | 说明                     |
|----------|--------------------|--------------------------|
| **后端**   | Python, Flask      | Web框架和编程语言        |
| **数据库** | MySQL 8.0+         | 关系型数据库管理系统     |
| **前端**   | Bootstrap, HTML5   | UI框架和数据可视化库    |
| **工具**   | Git, pip, dotenv   | 版本控制，管理依赖，管理环境  |

### 📝 使用指南

#### 添加学生:

- 1.点击"添加新学生"框

- 2.填写学生姓名、班级和各科成绩（0-100分）

- 3.点击"提交"保存记录

#### 批量导入:

- 1.准备CSV文件（格式：姓名,班级,语文,数学,英语,计算机）

- 2.在"批量导入"页面拖放或选择文件

- 3.系统自动验证并导入数据

#### 数据分析:

- 学科分析：查看各科平均分、最高分、最低分

- 总分统计：分析班级/年级总分分布

- 分差计算：识别学科成绩差异

#### 成绩分析

- 学科分析：查看各科平均分、最高分、最低分

- 分差计算：识别学科成绩差异

#### 数据管理

- 删除记录：移除单个学生数据

- 重置系统：清空所有数据并恢复示例

### 🤝 贡献指南
欢迎提交 Issue 和 Pull Request!请遵循以下流程：

- 1.Fork 项目仓库

- 2.创建特性分支 (git checkout -b feature/new-feature)

- 3.提交更改 (git commit -am '添加新功能')

- 4.推送分支 (git push origin feature/new-feature)

- 5.创建 Pull Request

注意事项：

- 1.提交前确保通过所有测试

- 2.更新相关文档（如README）

- 3.遵循PEP 8代码规范

### 📄 许可证
本项目采用 MIT 许可证

提示：系统默认运行在6500端口，可通过修改app.py文件中的PORT配置项更改端口号。生产环境请设置DEBUG=False确保系统安全。
