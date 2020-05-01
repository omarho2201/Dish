from student import student

def crea_estudiantes(count_estudiantes):
    count = 0
    list_students = []
    while count < int(count_estudiantes):
        student_code = input("Escribe el número de matricula: ")
        student_name = input("Escribe el nombre: ")
        student_age = input("Escribe la edad: ")
        student_gender = input("Escribe el genero (M ó H): ")
        student_carreer = input("Escribe la carrera a la que pertenece: ")
        
        list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
        count = count + 1
        
    return list_students

def ordena_edades(list_students):
    E = 0
    list_orden = []
    list_orden = list_students
    list_orden.sort(key=lambda student: student.age, reverse=True)
    while E < len(list_orden):
        
        print(list_orden[E.get_name() + " " + list_orden[E].get_age())
        
        E = E + 1
    return 0

def separa_generos(list_students):
    X = 0
    eH = 0
    eM = 0
    i = 0
    list_H = []
    list_M = []
    while X < len(list_students):
        aux=list_students[X].get_gender()
        print(aux)
        if aux == "M":
            list_M[eM] = list_students[eM]
            eM = eM + 1
        if aux == "H":
            list_H[eH] = list_students[eH]
            eH = eH + 1
            X = X + 1
            
