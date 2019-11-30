# Birthday chocolate

#* len of chocolate bar should equal to birthday's month.
#* sum of number wirtten on chocolate bar should equal to the day of birthday.

def birthday(nums_on_chocolate_bars, day, month):
	ways = 0

	for counter, i in enumerate(range(month, len(nums_on_chocolate_bars) + 1)):
		if sum(nums_on_chocolate_bars[i - month: month + counter]) == day:
			ways += 1

	return ways