from os import listdir
from os.path import isfile, join

import time
watchDirectory = './results'
pollTime = 5 #in seconds

def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)       


def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if x not in OriginalList] 
    return(differencesList)    

def doThingsWithNewFiles(newFiles: list,watchDirectory:str):    
        print(f'file created{newFiles}')

def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals(): 
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(watchDirectory)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        doThingsWithNewFiles(fileDiff,watchDirectory)    

fileWatcher(watchDirectory, pollTime)