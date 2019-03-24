valid_test_cases = [
	([(1,5),(2,6)], True), # Overlapping, both positive
	([(1,5),(6,8)], False), # Non-overlapping, both positive
	([(2,6),(1,5)], True), # Overlapping, not in sorted order, both positive
	([(6,8),(1,5)], False), # Non-overlapping, not in sorted order, both positive
	([(-1,5),(2,6)], True), # Overlapping, one negative
	([(-1,5),(6,8)], False), # Non-overlapping, One negative
	([(2,6),(-1,5)], True), # Overlapping, not in sorted order, one negative
	([(6,8),(-1,5)], False), # Non-overlapping, not in sorted order, negatives
	([(-5,-1),(-6,-2)], True), # Overlapping, both negative
	([(-5,-1),(2,6)], False), # Non-overlapping, one negative
	([(1,5.4),(2.3,6)], True), # Overlapping, floats
]

invalid_test_cases = [
	[('1',5),(2,'6')], # Input values represented as string 
	[('1',5),('6','8')], # Input values represented as string 
]