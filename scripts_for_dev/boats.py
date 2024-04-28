import os,json,sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0])))
os.chdir(os.path.join(os.path.dirname(sys.argv[0]),".."))
from searchreplace import Replacer
path="BlueBlocksCraft 1.12.2/assets/minecraft/models/item/"

"""
    Overwrite this to change what file to be processed.
"""
def whetherToProcessFile(file:str):
    return file.endswith("_boat.json")

"""
    Overwrite this to change what operations to be done with the files.
"""
def operationToFiles(file:str):
    filename=os.path.basename(file)
    boatType=filename.removesuffix('_boat.json')
    with open(file,"r+") as f:
        data={
            "__comment": "Designed by Blue_Beaker",
            "parent":"item/shared/boats",
            "textures": {
                "texture": f"3dres/boat/boat_{boatType.replace('_','')}",
                "texture1": f"3dres/boat/boat_{boatType.replace('_','')}_2",
                "particle": f"items/{boatType}_boat"
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