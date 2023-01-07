#!python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	capitalLetterInLine = sum(1 for c in line if c.isupper()) 
	print('%s|%s'%(capitalLetterInLine, 1))