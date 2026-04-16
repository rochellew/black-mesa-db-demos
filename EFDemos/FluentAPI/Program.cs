using Microsoft.EntityFrameworkCore;
using FluentAPI.Data;

using var context = new BlackMesaContext();

var results = context.Employees
    .Include(e => e.Department)
    .ToList();

foreach(var emp in results)
{
    Console.WriteLine($"{emp.FirstName} {emp.LastName} ({emp.Department.DeptName})");
}