#!python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	lineLength = len(line)

	for lettersInRow in range(2,4):
		idx = lettersInRow-1
		while idx < lineLength:
			charactersDuplicated = True

			for i in range(1, lettersInRow):
				if line[idx] != line[idx-i]:
					charactersDuplicated = False
					break

			if charactersDuplicated:
				print('%s|%s'%(line[idx-(lettersInRow-1) : idx+1], 1))
				idx += lettersInRow
			else:
				idx +=1