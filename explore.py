import sys

# On several occasions, I have begun typing on my keyboard in one layout when I thought it was in another.
# As a double QWERTY/Dvorak user, this often results in meaningless strings "pgvd kjg;e"
# But now I wonder whether there are such pairs of words whose keystroke patterns are shared between
# QWERTY and DVORAK...

# Run this by passing in a dictionary.txt file in the command line args.


# Dict from QWERTY to Dvorak
qwertyToDvorak = {
	"Q": "\"",
	"W": "<",
	"E": ">",
	"R": "P",
	"T": "Y",
	"Y": "F",
	"U": "G",
	"I": "C",
	"O": "R",
	"P": "L",
	"A": "A",
	"S": "O",
	"D": "E",
	"F": "U",
	"G": "I",
	"H": "D",
	"J": "H",
	"K": "T",
	"L": "N",
	";": "S",
	"Z": ";",
	"X": "Q", 
	"C": "J",
	"V": "K",
	"B": "X",
	"N": "B",
	"M": "M",
	",": "W",
	".": "V",
	"/": "Z",
}

def findMatch(word):
	matched = []
	builtWord = ""
	for char in word:
		dvEquiv = qwertyToDvorak.get(char.upper(), "@")
		builtWord += dvEquiv

	if builtWord in words and builtWord:
		matched.append(builtWord)

	return matched

if len(sys.argv) != 2:
	print('Usage: python explore.py <dictionary-file>');
	sys.exit(len(sys.argv))

# read the file into words
words = [line.strip().upper() for line in open(sys.argv[1])]

# EXPERIMENTAL take 10000 words
words = words[:10000]

# for every word, try to find a match in dvorak
for word in words:
	matched = findMatch(word)
	print(matched)
