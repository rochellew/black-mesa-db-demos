using Microsoft.EntityFrameworkCore;
using AnnotationsSpectre.Data;
using Spectre.Console;

// so my dang symbols will show up in VS code terminal -_-
Console.OutputEncoding = System.Text.Encoding.UTF8;

const string ORANGE = "rgb(255,165,0)";

using var context = new BlackMesaContext();

var results = context.Employees
    .Include(e => e.Department)
    .ToList();

var table = new Table();
table.Border(TableBorder.Rounded);
// uncomment this if you want the table to expand the whole width of the terminal
//table.Expand();

AnsiConsole.Write(new Rule($"[{ORANGE} bold]\u03BB Black Mesa Employees[/]"));
table.AddColumn($"[{ORANGE} bold]Employee ID[/]");
table.AddColumn($"[{ORANGE} bold]Last Name[/]");
table.AddColumn($"[{ORANGE} bold]First Name[/]");
table.AddColumn($"[{ORANGE} bold]Department[/]");

bool alternate = false;
foreach(var emp in results)
{
    var color = alternate? "#AAA" : "#FFF";
    table.AddRow(
        $"[{color}]{emp.EmployeeId}[/]",
        $"[{color}]{emp.LastName}[/]",
        $"[{color}]{emp.FirstName}[/]",
        $"[{color}]{emp.Department.DeptName}[/]"
    );
    alternate = !alternate;
}

AnsiConsole.Write(new Align(table, HorizontalAlignment.Center));