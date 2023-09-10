import csv
import random

def split(inputFile, outPutName, lines):
    with open(inputFile,'r') as file:
        header = file.readline().strip()
        outputFile = None
        linecount = 0
        for line in file:
            if linecount % lines == 0:
                if outputFile is not None: #!=
                    outputFile.close()
                outputFile = open(f"{outPutName}_{linecount//lines}.csv",'w')
                outputFile.write(header+'\n')
            outputFile.write(line )
            linecount+=1
    if outputFile is not None:
        outputFile.close()

# comprobar solo ese archivo en especifico
if __name__ == "__main__":
    split("usuario.csv","Output",1000)