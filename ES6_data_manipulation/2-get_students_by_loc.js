// function that returns array of objects loacted in a city
export default function getStudentsByLocation(students, city) {
  // filter function gets students in specified city
  const studentList = students.filter((student) => student.location === city);

  //return the array of students in that city
  return studentList;
}
