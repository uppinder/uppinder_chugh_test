def check_overlap(P, Q):
	if P[0] > Q[0]:
		P, Q = Q, P

	return Q[0] >= P[0] and Q[0] < P[1]
