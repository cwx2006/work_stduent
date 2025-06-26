# controllers/student_controller.py
#前端
from flask import Blueprint, render_template, jsonify, request
from services.student_service import StudentService
from services.stats_service import SubjectStatistics

student_bp = Blueprint('student', __name__)
student_service = StudentService()


@student_bp.route('/')
def index():
    students_data = student_service.get_all_students()
    students_sorted = sorted(
        students_data,
        key=lambda s: s['cn'] + s['math'] + s['eng'] + s['cs'],
        reverse=True
    )

    stats = SubjectStatistics.calculate_statistics(students_data)
    return render_template('index.html',
                           statistics=stats,
                           student_count=len(students_data),
                           students=students_sorted)


@student_bp.route('/add_student', methods=['POST']) #添加学生
def add_student():
    data = request.form
    required_fields = ['name', 'classes', 'chinese', 'math', 'english', 'cs']

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"success": False, "message": f"缺少必填字段: {field}"}), 400

    try:
        chinese = float(data['chinese'])
        math = float(data['math'])
        english = float(data['english'])
        cs = float(data['cs'])
        for score in [chinese, math, english, cs]:
            score_flo = float(score) # 改过
            if score_flo < 0 or score_flo > 100:
                return jsonify({"success": False, "message": "成绩必须在0-100之间"}), 400
    except ValueError:
        return jsonify({"success": False, "message": "成绩必须是数字"}), 400

    # 调用服务层
    success = student_service.add_student({
        'name': data['name'],
        'classes': data['classes'],
        'chinese': chinese,
        'math': math,
        'english': english,
        'cs': cs
    })
    if not success:
        return jsonify({"success": False, "message": "数据库添加失败"}), 500

    return jsonify({"success": True, "message": "学生添加成功"})


@student_bp.route('/import_students', methods=['POST'])
def import_students():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "没有上传文件"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "没有选择文件"}), 400

    if not file.filename.lower().endswith(('.csv', '.txt')):
        return jsonify({"success": False, "message": "只支持CSV或TXT文件"}), 400

    try:
        success, message = student_service.import_students(file)
        if not success:
            return jsonify({"success": False, "message": message}), 400
        return jsonify({"success": True, "message": message})
    except UnicodeDecodeError:
        return jsonify({"success": False, "message": "文件编码错误，请使用UTF-8编码"}), 400
    except Exception as e:
        return jsonify({"success": False, "message": f"导入失败: {str(e)}"}), 500


@student_bp.route('/delete_student', methods=['POST'])
def delete_student():
    data = request.get_json()
    success, message = student_service.delete_student(data)

    if not success:
        return jsonify({"success": False, "message": message}), 400 if "缺少" in message else 404

    return jsonify({"success": True, "message": message})


@student_bp.route('/clear_data', methods=['POST'])
def clear_data():
    success, message = student_service.clear_data()
    if not success:
        return jsonify({"success": False, "message": "数据库重置失败"}), 500
    return jsonify({"success": True, "message": message})
