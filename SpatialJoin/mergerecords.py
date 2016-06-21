'''
Created on Mar 16, 2016
This script aims to merge two datasets based on their Tweet ID because the numbers of records do not match.
@author: edward
'''
from os.path import join
def fun_mergeData(strInputFile, strAppendFile, strOutputFile, inSep, appendSep):
    try:
        inRecords = []
        inFile = open(strInputFile)
        lines = inFile.readlines()
        inFile.close()
        for line in lines:
            line = line.strip()
            row = line.split(inSep)
            inRecords.append(row)
        appendRecords = dict()
        appendFile = open(strAppendFile)
        lines = appendFile.readlines()
        appendFile.close()
        for line in lines:
            line = line.strip()
            row = line.split(appendSep)
            if row[0] not in appendRecords.keys():
                appendRecords[row[0]] = row[1:len(row)]
            else:
                print row[0]
        print len(appendRecords)
        
        for r in inRecords:
            if r[0] in appendRecords.keys():
                mallet = appendRecords[r[0]]
                for m in mallet:
                    r.append(m)
            else:
                print r[0]
        outFile = open(strOutputFile, 'w')
        for r in inRecords:
            for i in range(0,len(r)):
                if i != len(r)-1:
                    outFile.write(r[i] +',')
                else:
                    outFile.write(r[i] + '\n')
        outFile.close()
    except Exception as e:
        print e.message
    pass

if __name__ == '__main__':
    strInputPath = 'E:/UsFood/results'
    strAppendPath = 'E:/UsFood/malletScore'
    strOutputPath = 'E:/UsFood/results'
    
    strInputFileNames = []
    strInputFileNames.append('resultFields')
    
    for i in range(17,23):
        strInputFileNames.append('resultFields'+str(i))
    for i in range(0,17):
        strInputFileNames.append('results'+str(i))
##    for i in range(6,17):
##        strInputFileNames.append('results'+str(i))
    strInputFiles = []
    strAppendFiles = []
    strOutputFiles = []
    for s in strInputFileNames:
        strInputFiles.append(s+'.txt')
        strAppendFiles.append(s+'.txt.MalletScore')
        strOutputFiles.append(s+'_r.txt')
    for i in range(0,len(strInputFiles)):
        strInputFile = strInputFiles[i]
        strAppendFile = strAppendFiles[i]
        strOutputFile = strOutputFiles[i]
        fun_mergeData(join(strInputPath,strInputFile), join(strAppendPath,strAppendFile), join(strOutputPath,strOutputFile), ',','\t')
    pass
