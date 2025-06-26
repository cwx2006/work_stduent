# services/stats_service.py
#统计
class SubjectStatistics:
    @staticmethod
    def calculate_statistics(students):     # 计算统计数据的逻辑
        if not students:
            return {
                "语文": {"avg": 0, "max": 0, "min": 100},
                "数学": {"avg": 0, "max": 0, "min": 100},
                "英语": {"avg": 0, "max": 0, "min": 100},
                "计算机": {"avg": 0, "max": 0, "min": 100},
                "总分": {"avg": 0, "max": 0, "min": 100}
            }

        cn_scores = [s['cn'] for s in students]
        math_scores = [s['math'] for s in students]
        eng_scores = [s['eng'] for s in students]
        cs_scores = [s['cs'] for s in students]
        total_scores = [s['cn'] + s['math'] + s['eng'] + s['cs'] for s in students]

        return {
            "语文": {
                "avg": SubjectStatistics.avg_score(cn_scores),
                "max": max(cn_scores) if cn_scores else 0,
                "min": min(cn_scores) if cn_scores else 0,
            },
            "数学": {
                "avg": SubjectStatistics.avg_score(math_scores),
                "max": max(math_scores) if math_scores else 0,
                "min": min(math_scores) if math_scores else 0,
            },
            "英语": {
                "avg": SubjectStatistics.avg_score(eng_scores),
                "max": max(eng_scores) if eng_scores else 0,
                "min": min(eng_scores) if eng_scores else 0,
            },
            "计算机": {
                "avg": SubjectStatistics.avg_score(cs_scores),
                "max": max(cs_scores) if cs_scores else 0,
                "min": min(cs_scores) if cs_scores else 0,
            },
            "总分": {
                "avg": SubjectStatistics.avg_score(total_scores),
                "max": max(total_scores) if total_scores else 0,
                "min": min(total_scores) if total_scores else 0,
            }
        }

    @staticmethod
    def avg_score(scores):    # 计算平均分的逻辑
        return sum(scores) / len(scores) if scores else 0