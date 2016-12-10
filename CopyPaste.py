'''
Created on 10 dec. 2016

@author: rober
'''

import json
#import wx
from os import path
import shutil

def main():
    print "Will copy files"
    jsonData = openConfigAsJson()
    copyFiles(jsonData)    

def openConfigAsJson():
    with open ('config.ini', 'r') as conf:
        jsonDataDict = json.loads(conf.read())
        print "JsonData: "+ str(jsonDataDict)
        return jsonDataDict
        
def copyFiles(pathsDict):
    abspath = path.abspath
    print str(abspath(pathsDict["FileToCopy"]["path"]))
    for copyToFile in pathsDict["CopyToFiles"]:
        shutil.copy(pathsDict["FileToCopy"]["path"],\
                    copyToFile["path"])


if __name__ == '__main__':
    main()