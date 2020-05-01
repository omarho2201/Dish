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
            
print("MUJERES: ")
        while i < eM:
                print(list_M[i].get_name() + " " + list_M[i].get_gender())
                print("HOMBRES: ")
        for i in list_H:
                print(list_H[i].get_name() + " " + list_H[i].get_gender())
                    
        return 0

def main():
    options = 1
    list_stud = []
    while options != "0":
        options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")
        if options == "1":
            print("crea estudiantes")
            count_x = input("cuantos estudiantes daremos de alta: ")
            list_stud = crea_estudiantes(count_x)
        if options == "2":
            print("ordena edades")
            li = list_stud
            ordena_edades(li)
        if options == "3":
            print("separa generos")
            li = list_stud
            separa_generos(li)
        
if _name_ == "main":
    main()
    
main()
