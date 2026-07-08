#Create student class that takes name and marks of 3 subjects as arguments in constructor.
#Then create a method to print average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is:", sum/3)
s1 = Student("Tony", [99,98,97])
s2 = Student("Stark", [65,98,75])
s3 = Student("Ironman", [86,78,99])

s1.get_avg()
s2.get_avg()
s3.get_avg()