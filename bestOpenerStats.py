wordsDict = {}
with open('bestOpenerResults.txt', 'r') as bestOpenerResultsFile:
    bestOpenerResultsLines = bestOpenerResultsFile.read().splitlines()
for line in bestOpenerResultsLines:
    lineWords = line.split()
    thisWord = lineWords[10]
    thisAvg = float(lineWords[13][:-1])
    thisMax = int(lineWords[15])
    wordsDict[thisWord] = (thisAvg, thisMax)
print(wordsDict)
