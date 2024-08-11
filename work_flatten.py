from copy import deepcopy
import json
import os,sys
import shutil
from os import path
import traceback
def flattenTexturesFolder(root):
    pwd=os.getcwd()
    os.chdir(root)
    files=treeSearch(".")
    changed={}
    for file in files:
        file = file.removeprefix("./")
        if file.endswith(".png") and file.find("/")>-1:
            changed["3dres/"+file.removesuffix(".png")]="3dres/"+file.replace("/","_").removesuffix(".png")
            if not dry_run:
                shutil.move(file,file.replace("/","_"))
    os.chdir(pwd)
    return changed
def treeSearch(root):
    fileList:list[str]=[]
    for file in os.listdir(root):
        filePath=path.join(root,file)
        if path.isdir(filePath) and not path.islink(filePath):
            fileList.extend(treeSearch(filePath))
        else:
            fileList.append(filePath)
    return fileList
def replaceInModels(modelsFolder,changeList:dict[str,str]):
    models=treeSearch(modelsFolder)
    for model in models:
        if not model.endswith(".json"):
            continue
        try:
            with open(model,"r") as f:
                data=f.read()
                data2=data
            for changeFrom in changeList:
                changeTo=changeList[changeFrom]
                data2=data2.replace(changeFrom,changeTo)
            if data2!=data:
                print(data2)
                if not dry_run:
                    with open(model,"w") as f:
                        f.write(data2)
                    
        except:
            print(model)
            traceback.print_exc()
    pass
dry_run=0
changed=flattenTexturesFolder("/mnt/G/Git/BlueBlocksCraft_Vanilla/BlueBlocksCraft 1.16/assets/minecraft/textures/3dres")
replaceInModels("BlueBlocksCraft 1.16/assets/minecraft/models",changed)
replaceInModels("BlueBlocksCraft 1.12.2/assets/minecraft/models",changed)
print(changed)