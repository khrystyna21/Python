from sql_class import *
from sqlalchemy import func

# for employee in session.query(Employees.first_name, Employees.last_name).all():
#       print(employee)

# for dep_id in session.query(Employees.department_id).distinct():
#     print(dep_id)

# for all in session.query(Employees).order_by(Employees.first_name.desc()):
#     print(all)

# max_salary = session.query(func.max(Employees.salary)).scalar()
# print(max_salary)
# min_salary = session.query(func.min(Employees.salary)).scalar()
# print(min_salary)

for dep in session.query(Employees).all():
    print(dep.department.department_name)






