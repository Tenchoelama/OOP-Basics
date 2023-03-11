#OOP

class Student():
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
            
        return value/len(self.students)
            
    
s1 = Student("Jack", 19, 95)
s2 = Student("bob", 19, 20)
s3 = Student("liv", 20, 99)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())



#Inheritence 



class Pet():
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
        
    def speak(self):
        print("meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} color.")
        
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("bow wow")
        
        
p = Pet("zema", 10)
p.show()
p.speak()

c = Cat("Singe", 1, "Yellow")
c.show()
c.speak()

d = Dog('Peter', 5, "Golden")
d.show()
d.speak()


        
        



