namespace FluentAPI.Models;

public class Department
{
    public int DeptId  {get;set;}
    public string DeptName {get;set;} = null!;
    public List<Employee> Employees {get;set;} = null!;
}