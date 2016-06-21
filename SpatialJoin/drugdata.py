'''
Created on Jan 28, 2016

@author: Dapeng Li
'''
import os.path

def fun_parseDrugData(strFileName, ch):
    if os.path.isfile(strFileName):
        try:
            print 'reading data from: ',strFileName
            f = open(strFileName)
            lines = f.readlines()
            print len(lines)
            data = lines[0:100]
            print lines[1].split(ch)[2]
            for i in range(1,100):
                strCoordinates = lines[i].split(ch)[2]
                start = strCoordinates.find('(')
                end = strCoordinates.find(')')
                coords =  strCoordinates[start+1:end].split(',')
                lat = coords[0]
                lon = coords[1]
#                 print lat,lon
            
        except Exception as e:
            print e.message
def fun_processData(strInputFile, strOutputFile):
    if os.path.isfile(strInputFile):
        try:
            f = open(strInputFile)
            lines = f.readlines()
            outfile = open(strOutputFile, 'w')
            for line in lines[1:len(lines)]:
                tweetID = line.split('\t')[0]
                strCoordinates = line.split('\t')[2]
                start = strCoordinates.find('(')
                end = strCoordinates.find(')')
                coords =  strCoordinates[start+1:end].split(',')
                lat = coords[0]
                lon = coords[1]
#                 print lat,lon
                row = tweetID + ',' + lat + ',' + lon + '\n'
                outfile.write(row)
            f.close()
            outfile.close()
        except Exception as e:
            print e.message    
def fun_extractData(strInputFile, strOutputFile, num):	
    if os.path.isfile(strInputFile):
        try:
            f = open(strInputFile)
            lines = f.readlines()
            outfile = open(strOutputFile, 'w')
            if num < len(lines):
                for line in lines[0:num-1]:
                    outfile.write(line)
            f.close()
            outfile.close()
        except Exception as e:
            print e.message
def fun_appendData(strInputFile, strAppendDataFile, strOutputFile, inSep, appendSep, appendCol):
    if os.path.isfile(strInputFile) and os.path.isfile(strAppendDataFile):
        with open(strOutputFile,'w') as outputFile:
            inputFile = open(strInputFile)
            inputlines = inputFile.readlines()
            appendFile = open(strAppendDataFile)
            appendlines = appendFile.readlines()
            print strInputFile
            print strAppendDataFile
            print len(inputlines), len(appendlines)
            #outputFile.write(inputlines[0].rstrip('\n') + '\t' + 'ZIP' + '\t' + 'TRACT' +'\n')
            for i in range(0,len(appendlines)):
                appendItems = appendlines[i].split(appendSep)
                if appendCol <len(appendItems):
                    line = inputlines[i].rstrip('\n') +  inSep + appendItems[appendCol].strip() + '\n'
                    #line = inputlines[i].rstrip('\n') +  appendItems[appendCol].strip() + '\n'
                    outputFile.write(line)
    else:
        print 'Error: files do not exist'    
    pass
if __name__ == '__main__':
    strInputPath = 'E:/coordinates'
    strAppendPath = 'E:/coordinates'
    strOutputPath = 'E:/coordinates/results'
    
#     fun_parseDrugData(os.path.join(strPath,'drug.csv'), ch='\t')
#     fun_parseDrugData(os.path.join(strPath,'drug.txt'), ch=',')
#     fun_parseDrugData(os.path.join(strPath,'drug_tract.txt'), ch=',')
#     fun_parseDrugData(os.path.join(strPath,'drug_zip.txt'), ch=',')
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
        strInputFiles.append(s+'_tract.txt')
        strAppendFiles.append(s+'_zip.txt')
        strOutputFiles.append(s+'_geo.txt')
    
    
    strOutputFile = os.path.join(strInputPath, 'test.csv')
#     fun_extractData(os.path.join(strPath,'drug.csv'), strOutputFile, 100)
#     fun_processData(os.path.join(strPath,'drug.csv'), os.path.join(strPath, 'drug.txt'))
    for i in range(0,len(strInputFiles)):
        strInputFile =  os.path.join(strInputPath, strInputFiles[i])
        strAppendFile =  os.path.join(strAppendPath, strAppendFiles[i])
        strOutputFile1 = os.path.join(strOutputPath, strOutputFiles[i])
        fun_appendData(strInputFile,strAppendFile, strOutputFile1,',',',',3)
    pass



