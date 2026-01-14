'''
Natthida Sriphan
663040479-3
P2
'''

from datetime import date
from University import *

print("===== PERSON =====")
p = Person("Tonnam", 30, "1995-01-01", "O", False)
print(p.display_info())

print("\n===== STAFF =====")
s = Staff("Mark", 40, "1985-05-12", "A", True, "IT", 2018)
s.set_salary(22000)
print(s.display_info())
print(s.get_salary())

print("\n===== PROFESSOR =====")
pr = Professor("Dr.Jaemin", 50, "1975-02-10", "B", True,
               "CS", 2012, 2, 1)
print(pr.display_info())

print("\n===== ADMINISTRATOR =====")
ad = Administrator("Jeno", 45, "1980-03-15", "AB", True,
                   "Finance", 2019, 3)
print(ad.display_info())

print("\n===== STUDENT =====")
g = [(3, "A"), (3, "B+"), (2, "B")]
st = Student("Patty", 20, "2005-06-20", "O", False,
             2023, "IT", "undergraduate", g)
print(st.display_info())

print("\n===== UNDERGRADUATE STUDENT =====")
ug = UndergraduateStudent("Haechan", 19, "2006-08-10", "A", False,
                           2024, "CS", [(3, "A"), (3, "A")])
ug.register_course("OOP")
ug.register_course("DS")
ug.club = "Coding"
print(ug.display_info())

print("\n===== GRADUATE STUDENT =====")
gs = GraduateStudent("Jisung", 24, "2001-04-12", "B", False,
                     2024, "DME", "Dr.Jaemin")
gs.set_thesis_name("Deep Learning")
gs.set_proposal_date(date(2025, 6, 1))
print(gs.display_info())
print(gs.get_graduation_date())
