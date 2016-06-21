# merge all data files into one file
import os
import os.path
if __name__ == '__main__':
    print 'start to merge all data files into one file'
    strDataPath = 'E:/drugAbuse/results_zip_tract'
    strOutputPath = 'E:/drugAbuse/statistics'
    strInputFileNames = []
    strInputFileNames.append('resultFields')
    
    for i in range(17,23):
        strInputFileNames.append('resultFields'+str(i))
    for i in range(0,17):
        strInputFileNames.append('results'+str(i))
    strInputFiles = []
    for s in strInputFileNames:
        strInputFiles.append(s+'_geo.txt')
    print strInputFiles
    outfile = open(os.path.join(strOutputPath,'test.txt'),'w')
    for f in strInputFiles:
        strFile = os.path.join(strDataPath,f)
        inputf = open(strFile)
        data = inputf.readlines()
        print f,len(data)
        inputf.close()
        for r in data:
            outfile.write(r)
    outfile.close()
    

