# models/student.py
# 学生类
class Student:
    def __init__(self, name, classes, cn, math, eng, cs):
        self.name = name
        self.classes = classes
        self.cn = float(cn)
        self.math = float(math)
        self.eng = float(eng)
        self.cs = float(cs)
        self.total_score = self.cn + self.math + self.eng + self.cs


#学生类