import shutil
import os
import glob
import csv

def moveFiles(src,dest,folderName,keyword):
    pattern = src + "\\*"+ keyword + "*"
    destFolder = os.path.join(dest,folderName)
    if(os.path.exists(destFolder) == False):
        os.mkdir(destFolder)
    for file in glob.iglob(pattern,recursive=True):
        if(os.path.isfile(file)):
            fileName = os.path.basename(file)
            dest1=os.path.join(destFolder,fileName)
            shutil.move(file,dest1)

while(True):
    continueInput = input("Continue organizing, yes('y') or no('n')? ")
    if(continueInput == "n"):
        break
    csvInput = input("Enter the path of the csv file: ")
    with open(csvInput) as csvFile:
        csvReader = csv.reader(csvFile,delimiter=",")
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                lineCount += 1
            else:
                moveFiles(row[0],row[1],row[2],row[3])
                lineCount += 1

