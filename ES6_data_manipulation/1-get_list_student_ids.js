// create a func with an array of ids
export default function getListStudentIds(studentList) {
  // Checks if argument studentList is an array
  if (!Array.isArray(studentList)) {
    // returns an empty array
    return [];
  }

  // create new array of ids
  const studentIds = studentList.map(students => students.id);

  // returns array of ids
  return studentIds;
}
