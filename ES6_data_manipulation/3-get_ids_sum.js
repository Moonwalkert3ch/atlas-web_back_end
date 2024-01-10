// function that returns sum of all the student ids
export default function getStudentIdsSum(studentList) {
  // reduce function to sum all student ids
  const sumOfIds = studentList.reduce((accumulator, student) => accumulator + student.id, 0);

  // return sum
  return sumOfIds;
}
