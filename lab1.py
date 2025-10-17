class Person:
    def show_Person(self):
        print("The hell was the Person")


class Student(Person):
    def show_Student(self):
        print("this is a student")


class Teacher(Person):
    def show_teacher(self):
        print("This is a teacher")


class PartTimeStudent(Student, Teacher):
    def show_Parttime(self):
        print("This is a part-time-student")


obj = PartTimeStudent()
obj.show_Person()
obj.show_teacher()
obj.show_Student()
obj.show_Parttime()