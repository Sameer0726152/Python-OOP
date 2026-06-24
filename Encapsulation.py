class Student:
    def __init__(self, name, grade, marks):
        self.name = name
        self._grade = grade
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
        
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")
        
    @property
    def grade(self):
        return self._grade
        
    @grade.setter
    def grade(self, value):
        if value in ["A", "B", "C", "F"]:
            self._grade = value
        else:
            print("Invalid grade")
        
    def report(self):
        print(f"Name: {self.name}, Grade: {self._grade}, Marks: {self.__marks}")

s1 = Student("Sam", "B", 80)
print(s1.marks)
print(s1.grade)
s1.report()
s1.marks = 90
s1.grade = "A"
s1.report()