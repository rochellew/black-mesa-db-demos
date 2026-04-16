using Microsoft.EntityFrameworkCore;
using FluentAPI.Models;

namespace FluentAPI.Data;

public class BlackMesaContext: DbContext
{
    public DbSet<Employee> Employees {get;set;}
    public DbSet<Department> Departments {get;set;}

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseNpgsql("Host=localhost;Port=5432;Database=coursedb;Username=student;Password=password123");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Department>(entity =>
        {
            entity.ToTable("departments", schema: "blackmesa");
            entity.HasKey(d => d.DeptId);
            entity.Property(d => d.DeptId).HasColumnName("dept_id");
            entity.Property(d => d.DeptName).HasColumnName("dept_name");
        });

        modelBuilder.Entity<Employee>(entity =>
        {
            entity.ToTable("employees", schema: "blackmesa");
            entity.HasKey(e => e.EmployeeId);
            entity.Property(e => e.EmployeeId).HasColumnName("employee_id");
            entity.Property(e => e.FirstName).HasColumnName("first_name");
            entity.Property(e => e.LastName).HasColumnName("last_name");
            entity.Property(e => e.DeptId).HasColumnName("dept_id");

            entity.HasOne(e => e.Department)
                .WithMany(d => d.Employees)
                .HasForeignKey(e => e.DeptId);
        });
    }
}