using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AnnotationsSpectre.Models;

[Table("employees", Schema = "blackmesa")]
public class Employee
{
    [Key]
    [Column("employee_id")]
    public int EmployeeId {get;set;}

    [Column("first_name")]
    [Required]
    public string FirstName {get;set;} = null!;

    [Column("last_name")]
    [Required]
    public string LastName {get;set;} = null!;

    [Column("dept_id")]
    public int DeptId {get;set;}

    [ForeignKey("DeptId")]
    public Department Department {get;set;} = null!;
}