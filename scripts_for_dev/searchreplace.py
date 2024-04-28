import os

class Replacer:
    def __init__(self,whetherToProcessFile,operationToFiles):
        self.whetherToProcessFile=whetherToProcessFile
        self.operationToFiles=operationToFiles
    def listTree(self,folder:str,recursive):
        files=[]
        files2=[]
        for file in sorted(os.listdir(folder)):
            path=os.path.join(folder,file)
            if recursive and os.path.isdir(path):
                files2.extend(self.listTree(path,recursive))
            elif self.whetherToProcessFile(path):
                files.append(file)
        files2.extend(files)
        return files2
    def run(self,scanPath:str,recursive:bool=True):
        os.chdir(scanPath)
        lst=self.listTree(scanPath,recursive)
        print(lst)
        for file in lst:
            self.operationToFiles(file)