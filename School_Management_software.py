users = {
    "students": [],
    "teachers": [],
    "homeroom_teachers": [],
}

def create_student():
    first_name = input("Eneter student's first name: ")
    last_name = input("Enter student's last name: ")
    class_name = input("Enter student class name: ")
    users["students"].append({"first_name": first_name, "last_name": last_name, "class_name": class_name})
    print("Student created succesfully.")
def create_teacher():
    first_name = input("Enter teacher's name: ")
    last_name = input("Enter teacher's last name: ")
    subjects = []
    while True:
        subject = input("Enter subject for the class(Or live blank to finish): ")
        if not subject:
            break
        subjects.append(subject)
    users["teachers"].append({"fitst_name": first_name, "last_name": last_name, "subject": subject})
    print("Teacher created succesfully.")

def create_homeroom_teacher():
    first_name = input("Enter homeroom teacher's first name: ")
    last_name = input("Enter homeroom teacher's last name: ")
    class_name = input("Enter homeroom teacher's class name: ")
    users["homeroom_teachers"].append({"fitst_name": first_name, "last_name": last_name, "class_name": class_name})
    print("Homeroom teacher created succesfully.")

def manage_class():
    class_name = input("Enter class name to manage: ")
    print(f"\nStudent in class {class_name}")
    for student in users["students"]:
        if student["class"] == class_name:
            print(f"{student['first_name']} {student['last_name']}")
    print("\nHomeroom teacher: ")
    for teacher in users["homeroom_teachers"]:
        if teacher["class"] == class_name:
            print(f"{teacher['first_name']} {teacher['last_name']}")
    print("")


def manage_students():
    name = input("Enter student's name: ")
    print(f"\nClased of {name}: ")
    for student in users["students"]:
        if student["first_name"] == name:
            print(student["class"])
            print("Teacher: ")
            for teacher in users["teachers"]:
                if student["class"] in teacher["subjects"]:
                    print(f"{teacher["first_name"]} {teacher['last_name']}")
                    break
    else:
        print("Student not found.")

def manage_teacher():
    name = input("Enter teacher's name: ")
    print(f"\nSubjects thought by {name}:")
    for teacher in users["teachers"]:
        if teacher["first_name"] == name:
            for subject in teacher["subjects"]:
                print(subject)
                break
    else:
        print("Teacher not found")

def manage_homeroom_teacher():
    name = input("Enter homeroom teacher's first name: ")
    print(f"\nClass lead by {name}:")
    for teacher in users["homeroom_teachers"]:
        if teacher["first_name"] == name:
            print(teacher["class"])
            print("Students: ")
            for student in users["students"]:
                if student["class"] == teacher["class"]:
                    print(f"{student['first_name']} {student["last_name"]}")
                    break
    else:
        print("Homeroom teacher not found.")

while True:
    print("\nAvailable commands :\n- create\n- manage\n- end")
    command = input("Enter command: ").lower()

    print(f"- {users}")
    if command == 'create':
        print("\nCreate options:\nstudent, teacher, homeroom teacher")
        create_option = input("Enter create option: ").lower()

        if create_option == 'student':
            create_student()
        elif create_option == 'teacher':
            create_teacher()
        elif create_option == 'homeroom teacher':
            create_homeroom_teacher()
        else:
            print("Invailid create option: ")

    elif command == 'manage':
        print("\nManage options:\nclass, student, homeroom teacher")
        manage_option = input("Enter manage option: ").lower

        if manage_option == 'class':
            manage_class()

        elif manage_option == 'student':
            manage_students()
        
        elif manage_option == 'teacher':
            manage_teacher()

        elif manage_option == 'homeroom teacher':
            manage_homeroom_teacher()

        else:
            print("Invailid manage option.")
            break
    
    elif command == 'end':
        break
    else:
        print("Invailid command.")
