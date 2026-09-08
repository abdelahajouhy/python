import os
import json
import shutil 
from datetime import datetime
from pathlib import Path
from utils import convert_date, isold, menage

folder = Path(r"C:\repos_local_git\Python-programming\file_manager\test_folder") # dossier des répértoire à tester, TODO: refactor later
containt = list(folder.glob('**/*.*')) # liste du contenu du répértoire de travaill
to_clean = folder.parents[0].joinpath('merde')
[x for x in folder.iterdir() if x.is_dir()] # on teste l'existe du répératoire de travail

files_info=dict()
total_size=0
files=[]
trash_files=[]
report = folder.parents[0].joinpath("report.json")

if os.path.exists(to_clean):
    print(f'** regarde ton fichier de merde, nettoie le et supprime le avant de vouloir me lancer, regarde dans **: \n{to_clean},')
    exit()

for file in containt:
    total_size+=file.stat().st_size
    files.append(file.name)
    files_info.update ({
        "folder": str(folder),
        file.name :{
            'path': file,
            'extention': file.suffix,
            'size': file.stat().st_size,
            'creation_date': convert_date(file.stat().st_ctime),
            'last_modification': convert_date(file.stat().st_mtime),
            'trash': isold(
                convert_date(file.stat().st_ctime), 
                convert_date(file.stat().st_mtime))
        }
    })

files_info.update({
        "number of file": len(containt),
        "total size": total_size,
        "disk percent usage": f'{(total_size/ shutil.disk_usage(folder).total)*100} %'
})

############# report 
with open(report,"w", encoding="utf-8") as f:
    json.dump(files_info,fp=f, sort_keys=True, indent=3,default=str)

#############  check des poubelles 

for f in files:
    if files_info[f]['trash']:
        trash_files.append(f)

if any(trash_files):
    os.mkdir(to_clean)

    for d in trash_files:
        src=files_info[d]["path"]
        print(src)
        print(to_clean)
        menage(source=src, destination=to_clean)


