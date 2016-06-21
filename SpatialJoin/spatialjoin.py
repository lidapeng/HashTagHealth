'''
Created on Apr 10, 2015
This Python script is used to perform a spatial join operation on geotagged tweets using census tract polygons.
Three Python libraries (shapely, fiona, and rtree) need to be installed before spatial join.
Note that the 64-bit version libraries are required for Windows (32-bit will not work for large datasets)

Last edited on: 4/15/2016
@author: Dapeng Li
'''
from shapely.geometry import shape
from shapely.geometry import Point
import fiona
import shapefile
import os.path
from rtree import index
#from numpy import record
import datetime


# A function for spatial join operation
# input parameters:
# strInputPtFile - input text file that contains geotagged tweets (format: ID, longitude, latitude)
# strPolygonFile - input shape file for census tract polygons 
# strGeoIDFieldName - input field name of the polygon data (the unique ID of each polygon. e.g., zip code)
# strOutputFile - output text file for the results (format: ID, longitude, latitude, GEOID)
def fun_spatialJoin(strInputPtFile, strPolygonFile, strOutputFile,strGeoIDFieldName):
    try:
        if os.path.exists(strInputPtFile) and os.path.exists(strPolygonFile):
            if os.path.exists(strOutputFile):
                os.remove(strOutputFile)
            print 'starting spatial join\n'
            startTime = datetime.datetime.now()
            print 'start time: ',startTime
            outputFile = open(strOutputFile,'w')
            # read polygon data
            print 'starting to read polygon data from: ', strPolygonFile
            polygons = [pol for pol in fiona.open(strPolygonFile)]
            # create spatial index
            print 'starting to create spatial index'
            idx = index.Index()
            for pos, poly in enumerate(polygons):
                idx.insert(pos, shape(poly['geometry']).bounds)
            
            print 'index constructed'
            # iterate each point in the file
            with open(strInputPtFile) as ptFile:
                for line in ptFile:
                    items = line.split(',')
                    strLon = items[2].strip()
                    strLat= items[1].strip()
                    tweetID = items[0].strip()
                    #print tweetID
                    if len(strLon)>0 and len(strLat)>0 and len(tweetID)>0 and is_float(strLat) and is_float(strLon):
                        longitude = float(strLon)
                        latitude = float(strLat)
                        # construct a point
                        pt = Point(longitude,latitude)
                        polyIDs =  list(idx.intersection(pt.bounds))
                        if len(polyIDs)>0:
                            bMatched = False
                            for j in polyIDs:
                                if pt.within(shape(polygons[j]['geometry'])):
                                    record = line.strip() + ',' + polygons[j]['properties'][strGeoIDFieldName] + '\n'
                                    #print j, polygons[j]['properties']['GEOID']
                                    outputFile.write(record)
                                    bMatched = True # it is matched
                                    #print record
                            if not bMatched:
                                record = line.strip() + ','+'\n'
                                outputFile.write(record)
                        else:
                            record = line.strip() + ','+'\n'
                            outputFile.write(record)
                    else:
                        continue
            outputFile.close()
            endTime = datetime.datetime.now()
            print 'end time: ',endTime
            print 'total time consumed: ', endTime-startTime
            print 'spatial join ended\n'
            # delete to release the memory
            del polygons
            del idx
            #gc.collect()
    except Exception as e:
        print e.message

if __name__ == '__main__':
    print 'starting spatial join'
    # the input file for geotagged tweets (format [id, latitude, longtitude])
 #   strInputFile = r'D:\Health Project\Twitter\0622 problem\coordinates_utah_3-5-15.txt'
  #  strInputFile = r'E:/UsCoordinates/results.txt'
     
     
#     strShpFile = r'D:\Health Project\Twitter\data\fionatest\tweets'
#     if not os.path.exists(strShpFile+'.shp'):
#         fun_createShpFromTxt(strInputFile, strShpFile)
    # the input file for census tracts (2010 census)
#     strUtahTractFile = r'D:\Data\2010Census\2010censustract\2010censustract.shp'
##strUSTractFile = r'D:\Data\2010Census\2010tractWGS84\2010tracts.shp'
    #strUSTractFile = r'D:\Data\ESRI2010Census\2010esricensustract.shp'  hh
    # 'GEOID10' is the field name for the US dataset
    strUSTractFile = r'E:/dapengdata/censustract/2010tracts.shp'
    strUtahTractFile = r'E:/dapengdata/censustract/utahcensustract.shp'
    strNYTractFile = r'E:/dapengdata/censustract/nycountytractst.shp'
    strSFTractFile = r'E:/dapengdata/censustract/sftracts.shp'
    # zip code area shapefiles
    # US national dataset (field name: ZIP)
    strUSZipcodeFile = r'E:/dapengdata/zipcode/uszipcode/uszipcode.shp'
    # Utah dataset (field name: ZIP5)
    strUtahZipcodeFile = r'E:/dapengdata/zipcode/utahzipcode/utahzipcode.shp'
#     strPointFile = r'D:\Health Project\Twitter\data\fionatest\tweets.shp'
##    strInputFile = r'E:/dapengdata/drugdata20160126/drug.txt'
##    strOutputFile = r'E:/dapengdata/drugdata20160126/drug_zip.txt'
    
    # test the spatial join function
    strGeoFile = strUSZipcodeFile
    strFieldName = 'ZIP'
    strPath = r'E:/coordinates/'

    # process one file
    #fun_spatialJoin(strInputFile,strGeoFile, strOutputFile, strFieldName )
    
    # batch processing (store al the file names in one array and iterate the array to perform spatial join for each file)
    strInputFileNames = []
    #strInputFileNames.append('resultFields')
    
    for i in range(17,23):
        #strInputFileNames.append('resultFields'+str(i))
        pass
    for i in range(2,17):
        strInputFileNames.append('results'+str(i))
    strInputFiles = []
    strOutputFiles = []
    for s in strInputFileNames:
        strInputFiles.append(s+'.txt')
        strOutputFiles.append(s+'_zip.txt')
    for i in range(0,len(strInputFiles)):
        strInputFile =  os.path.join(strPath, strInputFiles[i])
        strOutputFile = os.path.join(strPath, strOutputFiles[i])
        fun_spatialJoin(strInputFile,strGeoFile, strOutputFile, strFieldName)

    pass
