class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")   
        print(f"Age: {self.age}")



class Student(Person):
    def __init__(self, name, age, major, roll, marks):
        super().__init__(name,age)
        self.major = major
        self.roll = roll
        self.marks = marks

    def display_student_info(self):
        self.display_info()
        print(f"Major: {self.major}")   
        print(f"Roll: {self.roll}") 
        print(f"Marks: {self.marks}")

Person =  Person("Biwashhhh", 211)  
Person.display_info()

student= Student("Biwash",21,"Comp Sci","Com07",677)
student.display_student_info()
