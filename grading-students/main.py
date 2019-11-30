"""
! Problem

! FAIL : any grade is less than 40

? if the grades are (38 <= grade) .
	* if the diffrence between th grade and next multiple of 5-
	* - is 3 assign the grade to that number.

"""

def gradingStudents(grades):
	new_grades = []

	for grade in grades:
		if (grade < 38) :
			new_grades.append(grade)
		elif ( ((grade//5 + 1)*5) - grade ) < 3 :
				new_grades.append((grade//5 + 1)*5)
		else :
			new_grades.append(grade)
	
	return new_grades