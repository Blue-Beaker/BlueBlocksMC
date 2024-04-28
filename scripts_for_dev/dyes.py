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
    return file.endswith(".json") and 'dye_' in file

"""
    Overwrite this to change what operations to be done with the files.
"""
def operationToFiles(file:str):
    filename=os.path.basename(file)
    color=filename.removesuffix('.json').removeprefix('dye_')
    if color=="light_blue":
        color='lightblue'
    elif color=="silver":
        color='lightgray'
    with open(file,"r+") as f:
        data={
            "__comment": "Designed by Blue_Beaker",
            "parent":"item/shared/dyes",
            "textures": {
                "Bucket": "3dres/bucket",
                "dye": f"3dres/dye/{color}"
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