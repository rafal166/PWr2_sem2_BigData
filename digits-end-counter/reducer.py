import sys

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