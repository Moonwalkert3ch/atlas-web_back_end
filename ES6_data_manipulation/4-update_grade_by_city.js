// function that returns student by location and new grade

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // filter students by city
  const studentsByCity = studentList.filter((student) => student.location === city);

  // map grades for students by city
  const currentStudent = studentsByCity.map((student) => {

    // find new grade for current student
    const currentGrade = newGrades.find((grade) => grade.studentId === student.id);

    // add grade or n/a if not found
    const setGrade = currentGrade && currentGrade.grade || 'N/A';

    // returns object
    return { ...student, grade: setGrade };
  });

  // return new array
  return currentStudent;
}
