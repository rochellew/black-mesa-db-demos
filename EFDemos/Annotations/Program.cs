using Microsoft.EntityFrameworkCore;
using Annotations.Data;

using var context = new BlackMesaContext();

var results = context.Employees
    .Include(e => e.Department)
    .OrderBy(e => e.LastName)
    .ToList();

foreach(var emp in results)
{
    Console.WriteLine($"{emp.FirstName} {emp.LastName} ({emp.Department.DeptName})");
}