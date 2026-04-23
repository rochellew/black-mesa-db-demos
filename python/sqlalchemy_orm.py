from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, select, Column, Integer, String, ForeignKey, Date, Boolean
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

class Branch(Base):
    __tablename__ = "branches"
    __table_args__ = {"schema": "blackmesa"}
    branch_id = Column(Integer, primary_key=True)
    branch_name = Column(String)
    location = Column(String)
    established = Column(Date)
    is_underground = Column(Boolean)

BIODOME = Branch(
    branch_id = 6, # note that if you don't care about duplicate branch names, remove this line
    branch_name = "Bio-Dome Research",
    location = "Sector E, Biodome Complex",
    established = "1994-05-12",
    is_underground = True
)

COLORS = {
    "ORANGE"  : "rgb(255,165,0)",
    "BLUE"    : "rgb(0,200,255)",
    "PURPLE"  : "rgb(198,152,245)"
}

def show_employees_by_dept(accent_color):
    console.print(Rule(f"[{accent_color} bold]\u03BB Black Mesa Employees[/]"))

    columns = ["Employee ID", "First Name", "Last Name", "Department"]
    table = create_table(accent_color, columns)

    with Session(engine) as session:
        results = session.query(Employee, Department)\
            .join(Department, Employee.dept_id == Department.dept_id)\
            .all()

        for i, (emp, dept) in enumerate(results):
            table.add_row(
                f"{emp.employee_id}",
                f"{emp.first_name}",
                f"{emp.last_name}",
                f"{dept.dept_name}"
            )


    console.print(table, justify="center")

def branches_ddl_dml(accent_color, new_branch = None):
    console.print(Rule(f"[{accent_color} bold]\u03BB Black Mesa Branches[/]"))

    TEMP_ID = 6

    columns = ["Branch ID", "Branch Name", "Location", "Date Established", "Underground"]
    table = create_table(accent_color, columns)
    target_id = None

    with Session(engine) as session:
        existing = session.get(Branch, TEMP_ID)
        if existing:
            session.delete(existing)
            session.commit()

        if new_branch:
            session.add(new_branch)
            session.commit()
            target_id = new_branch.branch_id

        results = session.query(Branch).all()

    for branch in results:
        color = "green" if branch.branch_id == target_id else ""
        row_data=[
            f"[{color}]{getattr(branch, col.key)}[/]" if color else
            str(getattr(branch,col.key)) for col in branch.__mapper__.columns
        ]
        table.add_row(*row_data)

    console.print(table, justify="center")

def update_employee(accent_color):
    console.print(Rule(f"[{accent_color} bold]\u03BB Black Mesa Branches[/]"))

    columns = ["Employee ID", "First Name", "Last Name"]
    table = create_table(accent_color, columns)

    with Session(engine) as session:
        target_emp = session.get(Employee, 15)
        if target_emp:
            target_emp.first_name = "Dr." if target_emp.first_name == "Arne" else "Arne"
            session.commit()

            session.refresh(target_emp)

            table.add_row(
                str(target_emp.employee_id), 
                f"[green bold]{target_emp.first_name}[/]",
                target_emp.last_name,
            )
        else:
            console.print("[red]Error: Employee 15 (Magnusson) not found.")

    console.print(table, justify="center")

def create_table(accent_color, columns):
    table = Table(
        box=box.ROUNDED,
        row_styles=["#FFFFFF","#BCBCBC"]      
    )
    for col in columns:
        table.add_column(f"[{accent_color} bold]{col}[/]")
    return table

show_employees_by_dept(COLORS["ORANGE"])
branches_ddl_dml(COLORS["BLUE"])
branches_ddl_dml(COLORS["BLUE"], BIODOME)
update_employee(COLORS["PURPLE"])
