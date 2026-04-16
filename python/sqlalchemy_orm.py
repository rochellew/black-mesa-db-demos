from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich import box

console = Console()

engine = create_engine("postgresql+psycopg2://student:password123@localhost:5432/coursedb")

class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "blackmesa"}

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String)

class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {"schema": "blackmesa"}

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dept_id = Column(Integer, ForeignKey("blackmesa.departments.dept_id"))

ORANGE = "rgb(255,165,0)"

console.print(Rule(f"[{ORANGE} bold]\u03BB Black Mesa Employees (SQLAlchemy - ORM)[/]"))

table = Table(box=box.ROUNDED)
table.add_column(f"[{ORANGE} bold]Employee ID[/]")
table.add_column(f"[{ORANGE} bold]Last Name[/]")
table.add_column(f"[{ORANGE} bold]First Name[/]")
table.add_column(f"[{ORANGE} bold]Department[/]")

with Session(engine) as session:
    results = session.query(Employee, Department)\
        .join(Department, Employee.dept_id == Department.dept_id)\
        .all()

    for i, (emp, dept) in enumerate(results):
        color = "#AAAAAA" if i % 2 == 0 else "#FFFFFF"
        table.add_row(
            f"[{color}]{emp.employee_id}[/]",
            f"[{color}]{emp.last_name}[/]",
            f"[{color}]{emp.first_name}[/]",
            f"[{color}]{dept.dept_name}[/]"
        )

console.print(table, justify="center")