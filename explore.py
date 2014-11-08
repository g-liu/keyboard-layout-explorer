import sys

# On several occasions, I have begun typing on my keyboard in one layout when I thought it was in another.
# As a double QWERTY/Dvorak user, this often results in meaningless strings "pgvd kjg;e"
# But now I wonder whether there are such pairs of words whose keystroke patterns are shared between
# QWERTY and DVORAK...

# Run this by passing in a dictionary.txt file in the command line args, and specifying the conversion mode:
# either one of -dq or -qd. Run `py explore.py` to learn more.


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
	" ": " ",
	"-": "[",
}
dvorakToQWERTY = {v: k for k, v in qwertyToDvorak.items()}

def getDvorakEquiv(word):
	return "".join([qwertyToDvorak.get(char.upper(), char) for char in word])

def getQWERTYEquiv(word):
	return "".join([dvorakToQWERTY.get(char.upper(), char) for char in word])

if len(sys.argv) != 3:
	print('Usage: python explore.py <dictionary-file> <conversion-direction>')
	print("\tconversion-direction: one of -qd or -dq")
	print("\t\t-qd: QWERTY to Dvorak")
	print("\t\t-dq: Dvorak to QWERTY")
	sys.exit(len(sys.argv))

# read the file into words
words = set([line.strip().upper() for line in open(sys.argv[1])])

# for every word, try to find a match in dvorak
for word in words:
	if sys.argv[2] == "-qd":
		dWord = getDvorakEquiv(word)
		if dWord in words:
			print("%s\t%s" %(word, dWord))
	elif sys.argv[2] == "-dq":
		qWord = getQWERTYEquiv(word)
		if qWord in words:
			print("%s\t%s" %(word, qWord))
	else:
		print("Error: invalid parameter %s" %(sys.argv[2]))
