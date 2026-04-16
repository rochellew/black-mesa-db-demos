using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Annotations.Models;

[Table("departments", Schema = "blackmesa")]
public class Department
{
    [Key]
    [Column("dept_id")]
    public int DeptId  {get;set;}

    [Column("dept_name")]
    [Required]
    public string DeptName {get;set;} = null!;

    public List<Employee> Employees {get;set;} = null!;
}