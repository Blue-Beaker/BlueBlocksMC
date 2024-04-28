import os,json,sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0])))
os.chdir(os.path.join(os.path.dirname(sys.argv[0]),".."))
from searchreplace import Replacer
path="BlueBlocksCraft 1.12.2/assets/minecraft/models/item/"

path=os.path.abspath(path)
"""
    Overwrite this to change what file to be processed.
"""
def whetherToProcessFile(file:str):
    return file.endswith(".json") and ('_helmet' in file or '_chestplate' in file or '_leggings' in file or '_boots' in file)

"""
    Overwrite this to change what operations to be done with the files.
"""
def operationToFiles(file:str):
    filename=os.path.basename(file)
    split=filename.removesuffix('.json').split("_")
    material=split[0].replace('golden','gold')
    armorType=split[1]
    with open(file,"r+") as f:
        data={
            "__comment": "Designed by Blue_Beaker",
            "parent":f"item/shared/armor/{armorType}",
            "textures": {
                'texture' : f"3dres/armor/{material}_1",
                'texture1' : f"3dres/armor/{material}_2"
            }
        }
        print(json.dumps(data))
    if not data:
        return
    with open(file,"w") as f:
        json.dump(data,f)
    return

replacer=Replacer(whetherToProcessFile,operationToFiles)
replacer.run(os.path.abspath(path),False)