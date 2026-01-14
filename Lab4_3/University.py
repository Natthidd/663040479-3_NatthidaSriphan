'''
Natthida Sriphan
663040479-3
university
'''

from datetime import date, datetime

class Person:
    _running_number = 0

    def __init__(self, name, age, birthdate, bloodgroup, is_married):
        self.name = name
        self.age = age
        self._birthdate = birthdate
        self.__bloodgroup = bloodgroup
        self.__is_married = is_married
        self._id = self.__generate_id()

    def __generate_id(self):
        Person._running_number += 1
        current_year = datetime.now().year
        return f"{current_year}{Person._running_number:03d}"

    def display_info(self):
        return f"ID: {self._id}, Name: {self.name}, Age: {self.age}"

class Staff(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.department = department
        self.start_year = start_year
        self.tenure_year = self.__calculate_tenure()
        self.__salary = 0

    def __calculate_tenure(self):
        return datetime.now().year - self.start_year

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary = amount

    def display_info(self):
        return (super().display_info() +
                f", Department: {self.department}, Tenure: {self.tenure_year} years")


class Student(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.start_year = start_year
        self.major = major
        self.level = level
        self.grade_list = grade_list if grade_list else []
        self.gpa = self.calculate_instance_gpa()
        self.__graduation_date = self.__calculate_graduation_date()

    @staticmethod
    def calculate_gpa(credit_grade_list):
        grade_map = {
            "A": 4.0, "B+": 3.5, "B": 3.0,
            "C+": 2.5, "C": 2.0, "D": 1.0, "F": 0.0
        }
        total_points = 0
        total_credits = 0
        for credit, grade in credit_grade_list:
            total_points += credit * grade_map.get(grade, 0)
            total_credits += credit
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    def calculate_instance_gpa(self):
        return Student.calculate_gpa(self.grade_list)

    def __calculate_graduation_date(self):
        if self.level.lower() == "undergraduate":
            return self.start_year + 4
        else:
            return self.start_year + 2

    def display_info(self):
        return (super().display_info() +
                f", Major: {self.major}, Level: {self.level}, GPA: {self.gpa}")

class Professor(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, professorship, admin_position=0):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.professorship = professorship
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = (30000 +
                  self.tenure_year * 1000 +
                  self.professorship * 10000 +
                  self.admin_position * 10000)
        super().set_salary(salary)

    def display_info(self):
        return (super().display_info() +
                f", Professor Level: {self.professorship}, Salary: {self.get_salary()}")


class Administrator(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, admin_position):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = 15000 + self.tenure_year * 800 + self.admin_position * 5000
        super().set_salary(salary)

    def display_info(self):
        return (super().display_info() +
                f", Admin Level: {self.admin_position}, Salary: {self.get_salary()}")

class UndergraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         start_year, major, "undergraduate", grade_list)
        self.club = None
        self.course_list = []

    def register_course(self, course):
        self.course_list.append(course)

    def display_info(self):
        return (super().display_info() +
                f", Courses: {self.course_list}, Club: {self.club}")


class GraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, advisor_name):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         start_year, major, "graduate")
        self.advisor_name = advisor_name
        self.thesis_name = None
        self.__proposal_date = None
        self.__graduation_date = self._calculate_graduation_date()

    def _calculate_graduation_date(self):
        if self.__proposal_date:
            return self.__proposal_date.year + 1
        return datetime.now().year + 2

    def set_thesis_name(self, thesis):
        self.thesis_name = thesis

    def set_proposal_date(self, proposal_date):
        self.__proposal_date = proposal_date
        self.__graduation_date = self._calculate_graduation_date()

    def get_proposal_date(self):
        return self.__proposal_date

    def get_graduation_date(self):
        return self.__graduation_date

    def display_info(self):
        return (super().display_info() +
                f", Advisor: {self.advisor_name}, Graduation Year: {self.__graduation_date}")
