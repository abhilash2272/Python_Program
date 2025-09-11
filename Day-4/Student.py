class Student:
    def __init__(self,name,roll,marks):
        self.__name=name#private variable
        self.roll=roll#public variable
        self._marks=marks#protected variable
    def display(self):
        print(f"{self.__name} got marks {self._marks} of roll number {self.roll}")
s=Student("abhi","5KY",97)
s1=Student("shiva","69",98)
s.display()
s1.display()    