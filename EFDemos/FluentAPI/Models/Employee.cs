namespace FluentAPI.Models;

public class Employee
{
    public int EmployeeId {get;set;}
    public string FirstName {get;set;} = null!;
    public string LastName {get;set;} = null!;
    public int DeptId {get;set;}
    public Department Department {get;set;} = null!;
}