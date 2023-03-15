list = []


def studentsTakeTheList():
    name = input("Enter the student's name : ")
    surname = input("Enter the student's Surname : ")
    if not name.isalpha() and not surname.isalpha():
        print("No input other than alphanumeric characters")
        return ""
    return (name.title() + " " + surname.title()).strip()

def studentsAppendTheList():
    student = studentsTakeTheList()
    if not student == "":
        list.append(student)

def studentsMultipleAppendTheList():
    count = int(input("Please enter the student count : "))
    for i in range(count):
        studentsAppendTheList()

def printStudents():
    for student in list:
        print(student)


def schoolNumber():
    student = studentsTakeTheList()
    if student not in list:
        print("Student not exists.")
        return
    print("student number : " + str(list.index(student)))

def removeStudentMultiple():
    while True:
        student = input("Please enter the student name and surname : ").title().strip()

        if student == "Q" or student == "q":
            break

        if  student not in list:
            print("Student not exists.")
            continue

        list.remove(student)
        print("student removed.")
        if len(list) == 0:
            print("All students removed.")
            break



print(list)