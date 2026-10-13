from datetime import datetime, timedelta
import shutil
import logging

LIMIT_DAY = 180  # 6 months, you can change it.

def convert_date(x):
    return datetime.fromtimestamp(x)

def isold(creation_date, modification_date):
    now = datetime.now()
    age = now - creation_date
    age_limite = timedelta(days=LIMIT_DAY)
    inactivity = now - modification_date
    if age > age_limite or inactivity > age_limite:
        return True
    else:
        return False

def menage(source, destination):
    logging.info(f"Déplacement : {source} -> {destination}")
    shutil.move(str(source), str(destination))
