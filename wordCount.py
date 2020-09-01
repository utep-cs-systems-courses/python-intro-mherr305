#!/usr/bin/env python3

import re   #Regular exp tool
import sys  #Command line
import os   #Check if file exists

#set the input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

#Cheking if the text file exist.
if not os.path.exists(inputFileName):
    print("The program does not exist.Please try another text file")
    exit()

#In these next lines opens the document use lower case and revome any punctuaction.
inputTextFile = open(inputFileName, "r")

for line in inputTextFile:
    line = line.lower()
    line = re.sub('[^\w\s]', '', line)
    line = line.strip()
    textWords = line.split()
