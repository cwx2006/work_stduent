# services/student_service.py
#学生数据修改
from models.student import Student
from models.database import DBManager
class BaseService:
    def log_error(self, message):
        print(f"[ERROR] {message}")

class StudentService:
    def __init__(self):
        self.db_manager = DBManager()

    def get_all_students(self):
        return self.db_manager.get_all_students()

    def add_student(self, data):
        try:
            return self.db_manager.add_student(
                data['name'], data['classes'],
                int(data['chinese']), int(data['math']),
                int(data['english']), int(data['cs'])
            )

        except Exception as e:
            self.log_error(f"添加学生失败: {str(e)}")  # 使用继承的方法
            return False

    def import_students(self, file):
        students = []
        contents = file.stream.read().decode("utf-8")
        lines = contents.split('\n')

        for i, line in enumerate(lines):
            if not line.strip():
                continue

            data = line.strip().split(',')
            if len(data) < 6:
                return False, f"第 {i + 1} 行格式不正确，需要6个字段"

            try:
                students.append({
                    'name': data[0],
                    'classes': data[1],
                    'cn': int(data[2]),
                    'math': int(data[3]),
                    'eng': int(data[4]),
                    'cs': int(data[5])
                })

                for score in [int(data[2]), int(data[3]), int(data[4]), int(data[5])]:
                    if score < 0 or score > 100:
                        return False, f"第 {i + 1} 行成绩超出范围：{score}"
            except ValueError:
                return False, f"第 {i + 1} 行成绩字段无效：{data[2:6]}"

        success = self.db_manager.import_students(students)
        return success, f"成功导入 {len(students)} 条学生记录"

    def delete_student(self, data):
        name = data.get('name')
        classes = data.get('classes')
        if not name or not classes:
            return False, "缺少姓名或班级参数"
        return self.db_manager.delete_student(name, classes), "学生删除成功"

    def clear_data(self):
        return self.db_manager.clear_data(), "已清空所有数据并恢复默认示例"