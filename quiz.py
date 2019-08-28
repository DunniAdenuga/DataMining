import glob
import os
from operator import itemgetter

words = {}

# Read multiple files
listOfFiles = glob.glob(os.path.join('./Archive/', '???.txt'))
# print(listOfFiles)

for f in listOfFiles:
    input_text = open(f, 'r')
    fileLines = input_text.readlines()
    for line in fileLines:
        # strip line ends #########################
        lineWords = line.split()
        for lineWord in lineWords:
            lineWord = lineWord.lower()
            if lineWord in words:
                words[lineWord] = words.get(lineWord) + 1
            else:
                words[lineWord] = 1
    input_text.close()

# stackOverflow logic
listSW = sorted(words.items(), key=itemgetter(1), reverse=True)

i = 0
while i < 20:
    print(listSW[i][0] + ' ' + str(listSW[i][1]))
    print('\n')
    i = i + 1
