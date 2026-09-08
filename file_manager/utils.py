from datetime import datetime, timedelta
import shutil

LIMIT_DAY = 180 # 6 months for the production 


def convert_date(x):
    return datetime.fromtimestamp(x)

def isold(creation_date,modification_date):
    now = datetime.now()
    age = now - creation_date
    age_limite = timedelta(milliseconds=LIMIT_DAY) #days=LIMIT_DAY)
    inactivity = now - modification_date
    if age > age_limite or inactivity > age_limite:
        return True
    else:
        return False

def menage(source,destination):
    shutil.move(str(source),str(destination))


