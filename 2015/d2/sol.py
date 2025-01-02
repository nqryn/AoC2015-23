# Template
import argparse
import re


def read_in(test_mode: bool):
	f_name = 'f_test.in' if test_mode else 'f.in'
	boxes = []
	pattern = r'(?P<l>\d+)x(?P<w>\d+)x(?P<h>\d+)'
	with open(f_name) as f:
		for line in f:
			m = re.match(pattern, line)
			if m:
				l, w, h = m.group('l'), m.group('w'), m.group('h')
				boxes.append((int(l), int(w), int(h)))
	return boxes


def solve(boxes):
	wp = 0
	for (l, w, h) in boxes:
		sides = [l*w, l*h, w*h]
		wp += 2 * sum(sides) + min(sides)
	return wp


def solve2(boxes):
	ribbon = 0
	for (l, w, h) in boxes:
		wrap = 2 * ((l + w + h) - max(l, w, h))
		bow = l * w * h
		ribbon += wrap + bow
	return ribbon


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Process some flags.")
	parser.add_argument('--test', action='store_true', help="Run in test mode")
	args = parser.parse_args()

	in_values = read_in(args.test)
	res = solve2(in_values)
	
	print(f'Result: {res}')