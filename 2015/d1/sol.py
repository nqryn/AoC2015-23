# Template
import argparse


def read_in(test_mode: bool):
	f_name = 'f_test.in' if test_mode else 'f.in'
	# Define vars here
	with open(f_name) as f:
		for line in f:
			return line.strip()


def solve(data):
	floor = 0
	pos = 1
	basement_pos = 0
	for c in data:
		if c == '(':
			floor += 1
		else:
			floor -= 1
		pos += 1
		if floor == -1 and not basement_pos:
			basement_pos = pos
	return floor, basement_pos - 1


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Process some flags.")
	parser.add_argument('--test', action='store_true', help="Run in test mode")
	args = parser.parse_args()

	in_values = read_in(args.test)
	res = solve(in_values)
	
	print(f'Result: {res}')