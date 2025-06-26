# app.py
from flask import Flask  #使用这个框架
from controllers.student_controller import student_bp

app = Flask(__name__)
app.register_blueprint(student_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6500)#端口6500