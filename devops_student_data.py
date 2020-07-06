from student_data import Student

# Below we are initialising a class for a student with variables name, age and course.

class Devops(Student):
    def __init__(self, name, age, course):
        self.__name = name
        self.age = age
        self.__protected_course = course


# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def home(self):
        print(self.name + "is at home")

    def __change_course(self, course):
        self.course = course

# The above function 'change_course' is hidden because it has two underscores in front of it. This makes the function hidden because this is not a method we would need to use often.

m = Student("Mehdi", "21", "DevOps")

m.__change_course("Data")





