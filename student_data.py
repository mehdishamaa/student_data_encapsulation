# Below we are initialising a class for a student with variables name, age and course.

class Student():
    def __init__(self, name, age, course):
        self.__name = name
        self.age = age
        self.course = course


# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.


    def lunch(self):
        print(self.name + " " + "is on lunch")

    def home(self):
        print(self.name + "is at home")

    def __change_course(self, course):
        self.course = course

m = Student("Mehdi", "21", "DevOps")

m._Student__change_course("Data")







