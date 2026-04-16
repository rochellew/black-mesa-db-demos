from sqlalchemy import create_engine, text
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich import box

console = Console()

engine = create_engine("postgresql+psycopg2://student:password123@localhost:5432/coursedb")

ORANGE = "rgb(255,165,0)"

console.print(Rule(f"[{ORANGE} bold]\u03BB Black Mesa Employees (SQLAlchemy Core - No ORM)[/]"))

table = Table(box=box.ROUNDED)
table.add_column(f"[{ORANGE} bold]Employee ID[/]")
table.add_column(f"[{ORANGE} bold]Last Name[/]")
table.add_column(f"[{ORANGE} bold]First Name[/]")
table.add_column(f"[{ORANGE} bold]Department[/]")

with engine.connect() as conn:
    results = conn.execute(text("""
        SELECT e.employee_id, e.last_name, e.first_name, d.dept_name
        FROM blackmesa.employees e
        JOIN blackmesa.departments d ON e.dept_id = d.dept_id
        ORDER BY e.last_name, e.first_name
    """))
    for i, row in enumerate(results):
        color = "#AAAAAA" if i % 2 == 0 else "#FFFFFF"
        table.add_row(
            f"[{color}]{row[0]}[/]",
            f"[{color}]{row[1]}[/]",
            f"[{color}]{row[2]}[/]",
            f"[{color}]{row[3]}[/]"
        )

console.print(table, justify="center")