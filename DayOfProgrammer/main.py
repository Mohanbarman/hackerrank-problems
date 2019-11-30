"""
Hackerrank - Day Of Programmer.

1. Calculate day of the year in Russia.
2. Years -> 1700 - 2700

3. From 1700 to 1917 : Julian calender.
4. From 1919 : Gregorian calender.

5. 1918 of 31st jan : Julian calender.
	***After 31st jan 14th feb came in 1918***
6. 1918 of 14th feb : Gregorian calender.

* In both calenders february have 29 days during leap year

				Julian_calender
				      |
					  |	
		Leap years are divisible by 4.

  			 Gregorian_calender
			          |
			  		  |
	Leap years are divisible by 400 or 4 not 100.

"""

def dayOfProgrammer(y):
	if (y == 1918):
		return '26.09.1918'
	elif (y <= 1917 and y%4 == 0) or (y > 1917 and (y%400 == 0 or y%4 == 0 and (y%100 != 0))):
		return '12.09.' + str(y)
	else :
		return '13.09.' +str(y)
