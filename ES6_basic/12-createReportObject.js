export default function createReportObject(employeesList) {
  const employeeObject = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      const departmentCount = Object.keys(employeesList).length;

      return departmentCount;
    },
  };

  return employeeObject;
}
