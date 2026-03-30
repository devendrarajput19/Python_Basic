class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_details(self):
        print("Name: ", self.name)
        print("Roll_no: ", self.roll_no)
        print("Marks: ", self.marks)

    def cal_avg(self):
        average = sum(self.marks) / len(self.marks)
        return average
    
s1 = Student("Devendra", 1, [80, 85, 75, 50])
s2 = Student("Mahesh", 2, [90, 75, 80, 88])

# s1.display_details()
# s1.cal_avg()
# print("Average: ", s1.cal_avg())

students = [s1, s2]

for stud in students:
    stud.display_details()
    stud.cal_avg()
    print("Average: ", stud.cal_avg())