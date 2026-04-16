using Microsoft.EntityFrameworkCore;
using Annotations.Models;

namespace Annotations.Data;

public class BlackMesaContext: DbContext
{
    public DbSet<Employee> Employees {get;set;}
    public DbSet<Department> Departments {get;set;}

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseNpgsql("Host=localhost;Port=5432;Database=coursedb;Username=student;Password=password123");
}