class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_Students = sorted(student_list,key=lambda student:
                           student.cgpa,reverse=True)
  return sorted_Students

Students = [
      Student("Sharithi", "A123", 7.8),
      Student("Gabi", "A1234", 8.9),
      Student("Sharu", "A12345", 9.1),
      Student("Thiris", "A123456", 9.9),
  ]


sorted_Students = sort_students(Students)
for student in sorted_Students:
  print("Name: {},Roll number: {},cgpa{}".format(student.name,
                                                 student.roll_number,
                                                 student.cgpa))
