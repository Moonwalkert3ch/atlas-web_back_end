// function that returns student by location and new grade

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // filter students by city
  const studentsByCity = studentList.filter((student) => student.location === city);

  // map grades for students by city
  const currentStudent = studentsByCity.map((student) => {

    // find new grade for current student
    const currentGrade = newGrades.find((grade) => grade.studentId === student.id);

    // initialize variable
    let setGrade;

    //check if grade is found
    if (currentGrade) {
      setGrade = currentGrade.grade;
    } else {
      setGrade = 'N/A';
    }

    // returns object and value
    return { ...student, grade: setGrade };
  });

  // return new array
  return currentStudent;
}
