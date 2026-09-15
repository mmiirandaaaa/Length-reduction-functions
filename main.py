import utils
from math import lcm

exceptional: dict[int, list[int]] = utils.readtuples('exceptional_tuples.csv', ['degree', 'tuple'])
reduced: dict[int, list[int]] = dict()
lengths: list[dict[str,int]] = list()

for m in exceptional:
	tup: list[int] = utils.to_vector(exceptional[m],m)
	A: np.ndarray = utils.generators(m, reduced)
	x = utils.reduce(A,tup)
	red_tup = tup-A@x
	length = len(red_tup[red_tup!=0])
	if length <= 4:
		reduced[m] = utils.to_tuple(red_tup)
	else:
		tup: list[int] = utils.to_vector(utils.lift(exceptional[m],m,2*m),2*m)
		A: np.ndarray = utils.generators(2*m, reduced)
		x = utils.reduce(A,tup)
		red_tup = tup-A@x
		length = len(red_tup[red_tup!=0])
		if length <= 4:
			reduced[2*m] = utils.to_tuple(red_tup)

	lengths.append({'degree': m, 'length': length})
	print(f"m = {m}, length = {length}")
	print(reduced)

utils.writecsv(lengths, 'reduced_exceptional_tuples.csv', ['degree', 'length'])