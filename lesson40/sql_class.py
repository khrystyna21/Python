from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+pymysql://root:root-root21@localhost/hr')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Numeric, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    hire_date = Column(Date)
    job_id = Column(String)
    salary = Column(String)
    commission_pct = Column(Numeric)
    manager_id = Column(Numeric)
    department_id = Column(Numeric, ForeignKey('departments.department_id'))
    department = relationship('Departments', backref='employees')

    def __repr__(self):
        return "<Employees(employee_id='%s', first_name='%s', last_name='%s', email='%s', phone_number='%s', hire_date='%s', " \
               "job_id='%s', salary='%s', commission_pct='%s', manager_id='%s', department_id='%s')>" % (
            self.employee_id, self.first_name, self.last_name, self.email, self.phone_number, self.hire_date,
        self.job_id, self.salary, self.commission_pct, self.manager_id, self.department_id)

class Departments(Base):
    __tablename__ = 'departments'

    department_id = Column(Numeric, primary_key=True)
    department_name = Column(String)
    manager_id = Column(Numeric)
    location_id = Column(Numeric)

    def __repr__(self):
        return "<Departments(department_id='%s', department_name='%s', manager_id='%s', location_id='%s')>" % (
            self.department_id, self.department_name, self.manager_id, self.location_id)







