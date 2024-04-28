import os,json,sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0])))
os.chdir(os.path.join(os.path.dirname(sys.argv[0]),".."))
from searchreplace import Replacer
path="BlueBlocksCraft 1.12.2/assets/minecraft/models/item/"

filesMappings={
    "bottle_drinkable":'potion_bottle',
    "bottle_lingering":'potion_bottle_lingering',
    "bottle_splash":'potion_bottle_splash'
}
"""
    Overwrite this to change what file to be processed.
"""
def whetherToProcessFile(file:str):
    filename=os.path.basename(file)
    return filename.removesuffix('.json') in filesMappings

"""
    Overwrite this to change what operations to be done with the files.
"""
def operationToFiles(file:str):
    filename=os.path.basename(file)
    potionType=filesMappings.get(filename.removesuffix('.json'))
    with open(file,"r+") as f:
        data={
            "__comment": "Designed by Blue_Beaker",
            "parent":"item/shared/bottles",
            "textures": {
                "texture": f"3dres/{potionType}",
                "particle": "items/potion_overlay"
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