import subprocess
import uuid


def swap(x, y):
    return y, x

def genInfos():

        x = subprocess.check_output('wmic csproduct get UUID')
        x = str(x)
        x = x.replace("b", "")
        x = x.replace("'", "")
        x = x.replace(" ", "")
        x = x.replace("UUID", "")
        x = x.replace("\\", "")
        x = x.replace("n", "")
        x = x.replace("r", "")
        f= open("key","w")

        f.write(str(uuid.uuid4()).upper()+"\n")
        f.write(str(uuid.uuid1()).upper()+"\n")
        f.write(x.upper()+"\n")
        f.write(str(uuid.uuid4()).upper()+"\n")

        f.close()

genInfos()