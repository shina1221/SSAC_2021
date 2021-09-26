def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
students = [

    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 88, 95),
    create_student("구지연", 76, 98, 88, 95),
    create_student("나선주", 98, 98, 88, 95),
    create_student("윤아린", 65, 98, 88, 95),
    create_student("윤명월", 64, 98, 88, 95),
]
students = [
    {"name":"윤인성","koean":87, "math":98, "english":88, "science":95},
    {"name":"연하진","koean":92, "math":98, "english":96, "science":98},
    {"name":"구지연","koean":76, "math":96, "english":94, "science":90},
    {"name":"나선주","koean":98, "math":92, "english":96, "science":92},
    {"name":"윤아린","koean":65, "math":98, "english":98, "science":98},
    {"name":"윤명월","koean":64, "math":88, "english":92, "science":92}    
    ]
