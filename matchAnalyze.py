# Analyze the matches for certain patterns
# Use as: py matchAnalyze.py < match_file.txt
#
# Each line of the match file should consist of two strings separated by a tab space.
# The two strings correspond to the mapping from keystrokes in one layout to keystrokes
# in another layout.

import fileinput
import sys

# returns a tuple (first, second)
def tokenize(line):
	split = line.split("\t")
	if len(split) != 2:
		raise IOError("Invalid format on line: {line}".format(line=line))
	return (split[0], split[1])

# STATISTICAL FUNCTIONS BELOW
def countPercLetter(matches, letterSet):
	count = 0
	for tup in matches:
		for ltr in letterSet:
			if ltr.upper() in tup[0] or ltr.lower() in tup[0]:
				count += 1
				break

	return count * 100 / len(matches)

# Returns the distribution of word lengths
def getDistribution(matches):
	distr = dict()
	for tup in matches:
		length = len(tup[0])
		if length in distr:
			distr[length] += 1
		else:
			distr[length] = 0 # new key=>value pair

	return distr

if len(sys.argv) != 1:
	print('Usage: python matchAnalyze.py < match_file.txt')
	exit(len(sys.argv))

matches = list()
for line in fileinput.input():
	matches.append(tokenize(line.strip()))

# Get and print statistical info
distr = getDistribution(matches)
print("Total number of word pairs: {num}".format(num=len(matches)))
print("percent of pairs contain letter A: {percentA}%".format(percentA=round(countPercLetter(matches, set('A')), 2)))
print("percent of pairs contain letter M: {percentM}%".format(percentM=round(countPercLetter(matches, set('M')), 2)))
print("percent of pairs contain either letter A or letter M: {percentAorM}%".format(percentAorM=round(countPercLetter(matches, set(['A', 'M'])), 2)))
print("Distribution of word sizes: {distr}".format(distr=distr))
print("Percent distribution of word sizes {distPerc}"
	.format(distPerc=dict((k, round(v * 100 / sum(distr.values()), 2)) for k, v in distr.items())))
