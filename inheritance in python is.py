total_studen=0
total_amount_of_faculty=0
class curren_year_student():
    def __init__(self,faculty_name,student_count,symester_start_Date,symester_pess_of_student):
        self.faculy_name=faculty_name
        self.student_count=student_count
        self.sysmester_start_Date=symester_start_Date
        self.symester_pess_of_student=symester_pess_of_student
        self.total_amount_of_faculty
    def show_current_symester_detials(self):
        self.symester_pess_of_student
        self.total_amount_of_faculty=self.total_amount_of_faculty*self.symester_pess_of_student
      #  print("total pess of student:{}".format(self.student_pess))
        print("our faculty name is:{}".format(self.faculy_name))
        print("Total sudent:{}".format(self.student_count))
        print("start date of sudent:{}".format(self.sysmester_start_Date))
        print("Our symester pess is {}".format(self.symester_pess_of_student))
obj=curren_year_student("computer science",100,2014,21000)
obj.show_current_symester_detials()