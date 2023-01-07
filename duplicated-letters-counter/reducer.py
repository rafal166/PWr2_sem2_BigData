#!python
"""reducer.py"""

import sys

# Dostaje ciąg znaków "slowo|1"
# sumuje liczby występujące przy takich samych słowach

results = {}

for line in sys.stdin:
	line = line.strip()
	numberLetters, count = line.split('|')
	count = int(count)

	if results.get(numberLetters):
		results[numberLetters] += count
	else:
		results[numberLetters] = count

for key in results:
	print('%s:%s'%(key, results.get(key)))