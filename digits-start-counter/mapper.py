#!python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	lineLength = len(line)
	how_much_digits = 0

	for idx in range(0, lineLength): 
		if not line[idx].isdigit():
			break
		how_much_digits += 1

	if how_much_digits > 0:
		print('%s|%s'%(how_much_digits, 1))