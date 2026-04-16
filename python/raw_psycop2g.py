import psycopg2
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich import box

console = Console()

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="coursedb",
    user="student",
    password="password123"
)

cur = conn.cursor()
cur.execute("""
    SELECT e.employee_id, e.last_name, e.first_name, d.dept_name
    FROM blackmesa.employees e
    JOIN blackmesa.departments d ON e.dept_id = d.dept_id
    ORDER BY e.last_name, e.first_name
""")
rows = cur.fetchall()
cur.close()
conn.close()

ORANGE = "rgb(255,165,0)"

console.print(Rule(f"[{ORANGE} bold]\u03BB Black Mesa Employees (Raw psycop2g)[/]"))

table = Table(box=box.ROUNDED, title_style=f"{ORANGE} bold")
table.add_column(f"[{ORANGE} bold]Employee ID[/]")
table.add_column(f"[{ORANGE} bold]Last Name[/]")
table.add_column(f"[{ORANGE} bold]First Name[/]")
table.add_column(f"[{ORANGE} bold]Department[/]")

for i, row in enumerate(rows):
    color = "#AAAAAA" if i % 2 == 0 else "#FFFFFF"
    table.add_row(
        f"[{color}]{row[0]}[/]",
        f"[{color}]{row[1]}[/]",
        f"[{color}]{row[2]}[/]",
        f"[{color}]{row[3]}[/]"
    )

console.print(table, justify="center")