import subprocess

def swap(x, y):
    return y, x


def keyChecker():

        x = subprocess.check_output('wmic csproduct get UUID')
        x = str(x)
        x = x.replace("b", "")
        x = x.replace("'", "")
        x = x.replace(" ", "")
        x = x.replace("UUID", "")
        x = x.replace("\\", "")
        x = x.replace("n", "")
        x = x.replace("r", "")

        X = x.split("-")

        X[0], X[1] = swap(X[0], X[1])
        X[0], X[len(X)-1] = swap(X[0], X[len(X)-1])

        key = ''

        for s in X:
                for c in s:
                        key += str(c)
                        c = ord(c)
                        c = ((c % 2)*10 + (c))
                        c = hex(c)
                        c = c.replace("0x","")
                        key += c

        return key