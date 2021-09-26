students = [
    {"name":"윤인성","koean":87, "math":98, "english":88, "science":95},
    {"name":"연하진","koean":92, "math":98, "english":96, "science":98},
    {"name":"구지연","koean":76, "math":96, "english":94, "science":90},
    {"name":"나선주","koean":98, "math":92, "english":96, "science":92},
    {"name":"윤아린","koean":65, "math":98, "english":98, "science":98},
    {"name":"윤명월","koean":64, "math":88, "english":92, "science":92}    
    ]

print("이름", "총점", "평균", sep = "\t")

for student in students:
    score_sum = student['korean'] + student['math'] +\
        student['english'] + student['science']
    score_avarage = score_sum / 4
    print(student["name"], score_sum, score_avarage, sep="\t")
