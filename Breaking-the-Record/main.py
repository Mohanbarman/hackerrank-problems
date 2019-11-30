def breaking_records(scores):
	min_ = scores[0]
	max_ = scores[0]

	min_count = 0
	max_count = 0

	for score in scores:
		if score > max_ :
			max_ = score
			max_count += 1
		elif score < min_ :
			min_ = score
			min_count += 1
	
	return max_count, min_count