# question 5: You are creating a student grading system. Each student has a private attribute __grade representing their score. The class Student 
# should have methods set_grade(grade) to update the score, get_grade() to view it, and display_info() to show the student’s name and grade. Students should 
# create student objects, update grades using setters, retrieve them using getters, and understand how encapsulation keeps the grade secure from direct modification.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade    # private attribute

    def set_grade(self, grade):
        self.__grade = grade    # set private attribute

    def get_grade(self):
        return self.__grade    # return private attribute
    
    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.__grade}")

s = Student("Adeena", 'A')  # creating Student object
s.display_info()        # displaying original info

s.set_grade('A+')       # updating grade (private) thru setter
print("Updated Grade =", s.get_grade())  # print using getter

s.display_info() # displaying updated info
