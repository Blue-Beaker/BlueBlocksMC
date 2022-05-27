#! /bin/python3
import os,sys,shutil,json
from struct import pack
import re

from matplotlib.font_manager import json_dump
from numpy import math
os.chdir(sys.path[0])
input_pack="BlueBlocksCraft 1.12.2"
output_pack="BlueBlocksMC 1.8[Auto-Generated]"
mappingsTextureFolder={
#    "block/":"blocks/",
#    "item/":"items/"
}
mappingsTexture={
}
#for tree in ["acacia","birch","dark_oak","jungle","oak","spruce"]:
#    for block in [[f"{tree}_log",f"log_{tree}"],[f"{tree}_log_top",f"log_{tree}_top"],[f"{tree}_planks",f"planks_{tree}"],[f"{tree}_door_bottom",f"door_{tree}_lower"],[f"{tree}_door_top",f"door_{tree}_upper"],[f"{tree}_sapling",f"sapling_{tree}"],[f"{tree}_leaves",f"leaves_{tree}"]]:
#        mappingsTexture[f"block/{block[0]}"]=f"blocks/{block[1]}"
#init complete
input_path=input_pack
output_path=os.path.join("build/",output_pack)
os.makedirs("build",exist_ok=1)
if os.path.exists(output_path): #Asks if replace
    if input(f"{output_path} exists. Replace?[y/N]").lower() == "y":
        shutil.rmtree(output_path)
    else:
        print("Canceled.")
        exit()
shutil.copytree(input_path,output_path) #copies to output folder
os.chdir(output_path)
filelist=os.walk("./")           #get all files
os.makedirs("./assets/minecraft/textures/blocks",exist_ok=1)
os.makedirs("./assets/minecraft/textures/items",exist_ok=1)
for folder in filelist:
    for file in folder[2]:
        filepath=os.path.join(folder[0],file)
        if re.match(".*\.json",file):   #if it's a model or blockstates file
            try:
                with open(filepath,"r") as modelfile:
                    model=json.load(modelfile)
                try:
                    display=model["display"]
                    try:
                        display["firstperson"]["rotation"][1]=display["firstperson"]["rotation"][1]-45
                    except:
                        pass
                    for key in display.keys():
                        for i in range(0,3):
                            try:
                                display[key]["scale"][i]=min(display[key]["scale"][i]*1.6,4.0)
                            except:
                                pass
                    try:
                        displayGui=display["gui"]
                        displayGui["rotation"][0]=(displayGui["rotation"][0]-30)%360
                        displayGui["rotation"][1]=(displayGui["rotation"][1]-225)%360
                        displayGui["rotation"][2]=(displayGui["rotation"][2]-0)%360
                    except:
                        pass
                except:
                    pass
                json_dump(model,filepath)
            except Exception as exception:
                print(filepath,exception)
#        matchName=re.sub("(^\./assets/minecraft/textures/|\.(png|png\.mcmeta)$)","",filepath)
#        if matchName in mappingsTexture.keys():  #if it's to be moved
#            replaceName=mappingsTexture[matchName]
#            shutil.move(filepath,re.sub(matchName,replaceName,filepath))
#    matchName=re.sub("^\./assets/minecraft/textures/","",folder[0])
#    if matchName+"/" in mappingsTextureFolder.keys():
#        replaceName=mappingsTextureFolder[matchName+"/"]
#        shutil.move(folder[0],re.sub(matchName,replaceName,folder[0]))
with open("pack.mcmeta","r") as packmetafile:
    packmeta=json.load(packmetafile)
packmeta["pack"]["pack_format"]=1
json_dump(packmeta,"pack.mcmeta")
os.chdir("..")
shutil.make_archive(output_pack,"zip",output_pack)
