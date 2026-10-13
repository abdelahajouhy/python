import os
import json
import shutil
import platform
from datetime import datetime
from pathlib import Path
from utils import convert_date, isold, menage

folder = Path(input("`Paste the path of the folder you want to clean : "))

containt = list(folder.glob("**/*.*"))

os_name = platform.system()

if os_name == "Windows":
    desktop = Path.home() / "Desktop"
elif os_name == "Darwin":
    desktop = Path.home() / "Desktop"
elif os_name == "Linux":
    desktop = Path.home() / "Desktop"
else:
    raise OSError(f"Unsupported operating system : {os_name}")

to_clean = desktop / "mess"
report = desktop / "report.json"

[x for x in folder.iterdir() if x.is_dir()]

files_info = dict()
total_size = 0
files = []
trash_files = []

if os.path.exists(to_clean):
    print(
        f"** Check the folder to clean, clean it, and delete it before attempting to launch **: \n{to_clean},"
    )
    exit()

for file in containt:
    total_size += file.stat().st_size
    files.append(file.name)
    files_info.update(
        {
            "folder": str(folder),
            file.name: {
                "path": file,
                "extention": file.suffix,
                "size": file.stat().st_size,
                "creation_date": convert_date(file.stat().st_ctime),
                "last_modification": convert_date(file.stat().st_mtime),
                "trash": isold(
                    convert_date(file.stat().st_ctime),
                    convert_date(file.stat().st_mtime),
                ),
            },
        }
    )

files_info.update(
    {
        "number of file": len(containt),
        "total size": total_size,
        "disk percent usage": f"{(total_size/ shutil.disk_usage(folder).total)*100} %",
    }
)

############# report #############
with open(report, "w", encoding="utf-8") as f:
    json.dump(files_info, fp=f, sort_keys=True, indent=3, default=str)

############# Check the trash #############
print(trash_files)
for f in files:
    if files_info[f]["trash"]:
        trash_files.append(f)

if any(trash_files):
    os.mkdir(to_clean)

    for d in trash_files:
        src = files_info[d]["path"]
        print("CALL CLEAN :", src)
        print(to_clean)
        menage(source=src, destination=to_clean)
