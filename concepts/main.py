# Example of a class

class Student:

    def __init__(self, firstname, lastname, age=None):
        self.firstname = firstname
        self.lastname = lastname
        if age is None:
            self.age = ''
        else:
            self.age = age

    def get_student_info(self):
        return self.firstname + " " + self.lastname + " " + str(self.age)


vinay = Student('Johnny', 'English', 12)
print(vinay.get_student_info())
